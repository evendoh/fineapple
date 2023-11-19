<template>
    <div class="space"></div>
    <div class="search">
      <form action="#">
        <label for="city">시도:</label>
        <select v-model="selectedCity" id="city">
          <!-- 여기에 시도 목록을 동적으로 채우는 옵션을 추가해야 합니다. -->
          <option value="seoul">서울특별시</option>
          <!-- 다른 시도들도 동일하게 추가 -->
        </select>
  
        <label for="district">시군구:</label>
        <select v-model="selectedDistrict" id="district">
          <!-- 여기에 시군구 목록을 동적으로 채우는 옵션을 추가해야 합니다. -->
          <option value="jongno">종로구</option>
          <!-- 다른 시군구들도 동일하게 추가 -->
        </select>
  
        <input type="submit" value="찾기" @click.prevent="searchLocation" />
      </form>
    </div>
    <div class="space"></div>
    <div id="map" style="width: 750px; height: 350px;"></div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import * as XLSX from 'xlsx';
  
  const selectedCity = ref('seoul');
  const selectedDistrict = ref('');
  
  onMounted(() => {
    initializeMap();
  });
  
  const initializeMap = () => {
    const mapContainer = document.querySelector('#map');
    const mapOption = {
      center: new kakao.maps.LatLng(37.56588, 126.97837),
      level: 3,
      mapTypeId: kakao.maps.MapTypeId.ROADMAP,
    };
    const map = new kakao.maps.Map(mapContainer, mapOption);
  
    // 엑셀 파일을 읽고 마커를 표시하는 함수
    const displayDistrictMarkers = (excelData) => {
      excelData.forEach((data) => {
        // 여기에서 각 데이터별로 마커를 생성 및 표시
        const districtMarker = new kakao.maps.Marker({
          position: new kakao.maps.LatLng(data.위도, data.경도),
          map: map,
        });
      });
    };
  
    // 초기에 마커 표시 (엑셀 데이터를 읽어오는 부분)
    readExcelFileAndDisplayMarkers();
  };
  
  const readExcelFileAndDisplayMarkers = async () => {
    const excelData = await readExcelFile(); // 엑셀 파일 읽기
    displayDistrictMarkers(excelData); // 읽은 데이터로 마커 표시
  };
  
  const readExcelFile = async () => {
    // 엑셀 파일 읽기
    const response = await fetch('@/assets/행정법정동.xlsx');
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: 'array' });
  
    // 엑셀 시트에서 데이터 추출
    const sheetName = workbook.SheetNames[0]; // 첫 번째 시트를 사용
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet);
  
    return jsonData;
  };
  
  const searchLocation = () => {
    console.log(`Selected City: ${selectedCity.value}`);
    console.log(`Selected District: ${selectedDistrict.value}`);
  };
  </script>
  
  <style>
  .space {
    height: 50px;
  }
  
  .search {
    margin-left: 100px;
  }
  
  #map {
    margin-left: 100px;
  }
  </style>
  