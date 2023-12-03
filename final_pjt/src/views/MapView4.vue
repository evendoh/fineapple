   <template>
    <div class="container">
      <h1>지도 검색</h1>
      <div class="search">
        <form action="#">
          <label for="city">시도:</label>
          <select v-model="selectedCity" id="city" @change="updateDistricts">
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
  import jsonData from '@/assets/data.json'

  console.log(jsonData)

  const selectedCity = ref('');
  const selectedDistrict = ref('');
  const cities = ref([]);
  const districts = ref([]);
  
  let map;
  
  // 지도 불러오기
  onMounted(async () => {
    await initializeDropdownLists(); // initializeDropdownLists 함수를 먼저 호출하여 jsonData를 초기화
    initializeMap();
    readJsondataFileAndDisplayMarkers();
  });
  
  // 시작 장소 지정
  const initializeMap = () => {
    const mapContainer = document.querySelector('#map');
    const mapOption = {
      center: new kakao.maps.LatLng(37.56588, 126.97837),
      level: 3,
      mapTypeId: kakao.maps.MapTypeId.ROADMAP,
    };
    map = new kakao.maps.Map(mapContainer, mapOption);
  };
  // 엑셀 파일을 읽고 마커를 표시하는 함수
  const displayDistrictMarkers = (jsonData) => {
    jsonData.DB.forEach((data) => {
      const districtMarker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(data.위도, data.경도),
        map: map,
      });
    });
  };
  // 초기에 마커 표시 (엑셀 데이터를 읽어오는 부분)
  const readJsondataFileAndDisplayMarkers = async () => {
    displayDistrictMarkers(jsonData); // jsonData를 사용하여 마커 표시
  };
  
  
// 드롭다운 목록 초기화 함수
const initializeDropdownLists = () => {
  cities.value = [...new Set(jsonData.DB.map((item) => item.시도))];
  districts.value = getDistrictsByCity(selectedCity.value, jsonData);
};

// 시도 변경 시 시군구 목록 업데이트 함수
const updateDistricts = () => {
  districts.value = getDistrictsByCity(selectedCity.value, jsonData);
};

// 시군구 목록 가져오기 함수
const getDistrictsByCity = (city, jsonData) => {
  const filteredData = jsonData.DB.filter((item) => item.시도 === city);
  return [...new Set(filteredData.map((item) => item.시군구))];
};

// 검색 버튼 클릭 시 실행 함수
const searchLocation = () => {
  console.log(`Selected City: ${selectedCity.value}`);
  console.log(`Selected District: ${selectedDistrict.value}`);
  // 여기에서 선택된 정보를 활용하여 원하는 동작 수행
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
  