
<template>
    <div class="space"></div>
    <div class="search">
    <form action="#">
      <label for="bank">은행 찾기</label>
      <select name="은행" id="bank">
        <option value="seoul">서울특별시</option>
        <option value="busan">부산광역시</option>
        <option value="daegu">대구광역시</option>
        <option value="incheon">인천광역시</option>
        <option value="kwangju">광주광역시</option>
        <option value="daejeon">대전광역시</option>
        <option value="ulsan">울산광역시</option>
        <option value="sejong">세종특별자치시</option>
        <option value="gg">경기도</option>
        <option value="k">강원도</option>
        <option value="cb">충청북도</option>
        <option value="cn">충청남도</option>
        <option value="jb">전라북도</option>
        <option value="jn">전라남도</option>
        <option value="kb">경상북도</option>
        <option value="kn">경상남도</option>
        <option value="jeju">제주도</option>
      </select>
      <select name="은행" id="bank">
        <option value="seoul">서울특별시</option>
        <option value="busan">부산광역시</option>
        <option value="daegu">대구광역시</option>
        <option value="incheon">인천광역시</option>
        <option value="kwangju">광주광역시</option>
        <option value="daejeon">대전광역시</option>
        <option value="ulsan">울산광역시</option>
        <option value="sejong">세종특별자치시</option>
        <option value="gg">경기도</option>
        <option value="k">강원도</option>
        <option value="cb">충청북도</option>
        <option value="cn">충청남도</option>
        <option value="jb">전라북도</option>
        <option value="jn">전라남도</option>
        <option value="kb">경상북도</option>
        <option value="kn">경상남도</option>
        <option value="jeju">제주도</option>
      </select>
      <select name="은행" id="bank">
        <option value="kukmin">국민은행</option>
        <option value="shinhan">신한은행</option>
        <option value="woori">우리은행</option>
        <option value="hana">하나은행</option>
        <option value="saneop">산업은행</option>
        <option value="nonghyeop">농협</option>
        <option value="saemaeul">새마을금고</option>
        <option value="shinhyeop">신협</option>
        <option value="post">우체국</option>
        <option value="kieop">기업은행</option>
        <option value="busan">부산은행</option>
        <option value="daegu">대구은행</option>
        <option value="kwangju">광주은행</option>
        <option value="kn">경남은행</option>
        <option value="jb">전북은행</option>
        <option value="jj">제주은행</option>
        <option value="sh">수협</option>
      </select>
      <!-- <input type="submit" value="찾기" /> -->
      <input type="submit" value="찾기" @click.prevent="searchLocation" />
      <!-- <input type="file" accept=".csv, appliction/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" /> -->
    </form>
  </div>
  <div class="space"></div>
  <div id="map" style="width:750px;height:350px;"></div>
    </template>
    
    <script setup>
import { ref, onMounted } from 'vue';

const selectedCity = ref('seoul'); // 선택된 도/시
const selectedDistrict = ref(''); // 선택된 구/군

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

  // 시군구 정보를 가져와서 마커를 표시하는 함수 (실제 데이터 소스에 따라 수정 필요)
  const displayDistrictMarkers = () => {
    // 여기에서 API 또는 데이터 소스로부터 시군구 정보를 가져와서 마커를 생성 및 표시
    // 예시로 하나의 마커를 표시하는 코드입니다.
    const districtMarker = new kakao.maps.Marker({
      position: new kakao.maps.LatLng(37.5665, 126.9780), // 실제 좌표로 수정
      map: map,
    });
  };

  // 초기에 마커 표시
  displayDistrictMarkers();
};

const searchLocation = () => {
  // 검색 버튼을 눌렀을 때 동작하는 함수 (시군구 정보 가져오기 등)
  // 예시로 선택된 도/시와 구/군을 출력하는 코드입니다.
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