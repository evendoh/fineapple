
   <template>
    <h1>Map4</h1>
    <div class="space"></div>
    <div class="search">
      <form action="#">
        <label for="city">시도:</label>
        <select v-model="selectedCity" id="city">
          <option v-for="city in cities" :value="city">{{ city }}</option>
        </select>
  
        <label for="district">시군구:</label>
        <select v-model="selectedDistrict" id="district">
          <option v-for="district in districts" :value="district">{{ district }}</option>
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
  
  const selectedCity = ref('');
  const selectedDistrict = ref('');
  const cities = ref([]);
  const districts = ref([]);
  let map;
  
  onMounted(async () => {
    initializeMap();
    await initializeDropdownLists();
    readExcelFileAndDisplayMarkers();
  });
  
  const initializeMap = () => {
    const mapContainer = document.querySelector('#map');
    const mapOption = {
      center: new kakao.maps.LatLng(37.56588, 126.97837),
      level: 3,
      mapTypeId: kakao.maps.MapTypeId.ROADMAP,
    };
    map = new kakao.maps.Map(mapContainer, mapOption);
  };
  
  const displayDistrictMarkers = (excelData) => {
    excelData.forEach((data) => {
      const districtMarker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(data.위도, data.경도),
        map: map,
      });
    });
  };
  
  const readExcelFileAndDisplayMarkers = async () => {
    const excelData = await readExcelFile();
    displayDistrictMarkers(excelData);
  };
  
  const readExcelFile = async () => {
    const response = await fetch('/행정법정동.xlsx');
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: 'array' });
  
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet);
    return jsonData;
  };
  
  const initializeDropdownLists = async () => {
    const excelData = await readExcelFile();
    cities.value = [...new Set(excelData.map((data) => data.시도))];
    districts.value = [...new Set(excelData.map((data) => data.시군구))];
    console.log('Cities:', cities.value);
    console.log('Districts:', districts.value);
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
  