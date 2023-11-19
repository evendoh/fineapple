<!-- 
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
   -->
<!-- 
   <template>
    <div class="container">
      <h1>지도 검색</h1>
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
      <div class="map-container">
        <div id="map"></div>
      </div>
    </div>
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
  body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    margin: 0;
  }
  
  .container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    text-align: center;
    color: #007BFF;
  }
  
  .search {
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    gap: 10px;
    align-items: center;
  }
  
  select,
  input {
    padding: 10px;
    font-size: 14px;
  }
  
  input[type="submit"] {
    background-color: #007BFF;
    color: #fff;
    cursor: pointer;
    border: none;
    border-radius: 5px;
  }
  
  input[type="submit"]:hover {
    background-color: #0056b3;
  }
  
  .map-container {
    margin-bottom: 20px;
  }
  
  #map {
    width: 100%;
    height: 300px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  </style>
   -->

   <template>
    <div class="container">
      <h1>지도 검색</h1>
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
          <label for="bank">은행:</label>
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
          <button @click.prevent="searchLocation">찾기</button>
        </form>
      </div>
      <div class="map-container">
        <div id="map"></div>
      </div>
    </div>
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
  };
  
  const searchLocation = () => {
    console.log(`Selected City: ${selectedCity.value}`);
    console.log(`Selected District: ${selectedDistrict.value}`);
  };
  </script>
  
  <style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    margin: 0;
  }
  
  .container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(30, 75, 76, 0.2);
  }
  
  h1 {
    text-align: center;
    color: #1E4B4C;
  }
  
  .search {
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    gap: 10px;
    align-items: center;
  }
  
  select,
  button {
    padding: 10px;
    font-size: 14px;
    border: 1px solid #1E4B4C;
    border-radius: 5px;
  }
  
  select {
    flex: 1;
  }
  
  button {
    background-color: #1E4B4C;
    color: #fff;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0D2C2D;
  }
  
  .map-container {
    margin-bottom: 20px;
  }
  
  #map {
    width: 100%;
    height: 300px;
    border: 1px solid #1E4B4C;
    border-radius: 10px;
  }
  </style>
  