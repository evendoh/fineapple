<template>
  <div class="map-wrap">
    <div id="map" style="width: 100%; height: 100%;"></div>
    <div id="menu-wrap" class="bg-white">
      <div class="option">
        <div>
          <form @submit.prevent="searchPlaces">
            <label for="city">시도:</label>
            <select v-model="selectedCity">
              <option v-for="city in cities" :key="city">{{ city }}</option>
            </select>
            <label for="district">시군구:</label>
            <select v-model="selectedDistrict">
              <option
                v-for="district in districts[selectedCity]"
                :key="district"
              >
                {{ district }}
              </option>
            </select>
            <label for="bank">은행:</label>
            <select v-model="selectedBank">
              <option v-for="bank in banks" :key="bank">{{ bank }}</option>
            </select>
            <button type="submit">검색</button>
          </form>
        </div>
      </div>
      <hr />
      <ul id="placesList"></ul>
      <div id="pagination"></div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const cities = ref([
      "서울시",
      "부산시",
      "대구시",
      "인천시",
      "광주시",
      "대전시",
      "울산시",
      "세종시",
      "제주도",
      "경기도",
      "강원도",
      "충청북도",
      "충청남도",
      "전라북도",
      "전라남도",
      "경상북도",
      "경상남도",
    ]);

    const districts = ref({
      서울시: [
        "종로구",
        "중구",
        "용산구",
        "성동구",
        "광진구",
        "동대문구",
        "중랑구",
        "성북구",
        "강북구",
        "도봉구",
        "노원구",
        "은평구",
        "서대문구",
        "마포구",
        "양천구",
        "강서구",
        "구로구",
        "금천구",
        "영등포구",
        "동작구",
        "관악구",
        "서초구",
        "강남구",
        "송파구",
        "강동구",
      ],
      부산시: [
        "중구",
        "서구",
        "동구",
        "영도구",
        "부산진구",
        "동래구",
        "남구",
        "북구",
        "강서구",
        "해운대구",
        "사하구",
        "금정구",
        "연제구",
        "수영구",
        "사상구",
      ],
      대구시: [
        "중구",
        "동구",
        "서구",
        "남구",
        "북구",
        "수성구",
        "달서구",
        "달성군",
        "군위군",
      ],
      인천시: [
        "중구",
        "동구",
        "미추홀구",
        "연수구",
        "남동구",
        "부평구",
        "계양구",
        "서구",
        "강화군",
        "옹진군",
      ],
      광주시: ["동구", "서구", "남구", "북구", "광산구"],
      대전시: ["동구", "중구", "서구", "유성구", "대덕구"],
      울산시: ["중구", "남구", "동구", "북구", "울주군"],
      세종시: [
        "조치원읍",
        "연기면",
        "연동면",
        "부강면",
        "금남면",
        "장군면",
        "연서면",
        "전의면",
        "전동면",
        "소정면",
        "한솔동",
        "새롬동",
        "나성동",
        "도담동",
        "어진동",
        "해밀동",
        "아름동",
        "종촌동",
        "고운동",
        "소담동",
        "반곡동",
        "보람동",
        "대평동",
        "다정동",
      ],
      경기도: [
        "수원시 장안구",
        "수원시 권선구",
        "수원시 팔달구",
        "수원시 영통구",
        "성남시 수정구",
        "성남시 중원구",
        "성남시 분당구",
        "의정부시",
        "안양시 만안구",
        "안양시 동안구",
        "부천시",
        "광명시",
        "동두천시",
        "평택시",
        "안산시 상로구",
        "안산시 단원구",
        "고양시 덕양구",
        "고양시 일산동구",
        "고양시 일산서구",
        "과천시",
        "구리시",
        "남양주시",
        "오산시",
        "시흥시",
        "군포시",
        "의왕시",
        "하남시",
        "용인시 처인구",
        "용인시 기흥구",
        "용인시 수지구",
        "파주시",
        "이천시",
        "안성시",
        "김포시",
        "화성시",
        "광주시",
        "양주시",
        "포천시",
        "여주시",
        "연천군",
        "가평군",
        "양평군",
      ],
      강원도: [
        "춘천시",
        "원주시",
        "강릉시",
        "동해시",
        "태백시",
        "속초시",
        "삼척시",
        "홍천군",
        "횡성군",
        "영월군",
        "평창군",
        "정선군",
        "철원군",
        "화천군",
        "양구군",
        "인제군",
        "고성군",
        "양양군",
      ],
      충청북도: [
        "청주시 상당구",
        "청주시 흥덕구",
        "청주시 서원구",
        "청주시 청원구",
        "충주시",
        "제천시",
        "보은군",
        "옥천군",
        "영동군",
        "증평군",
        "진천군",
        "괴산군",
        "음성군",
        "단양군",
      ],
      충청남도: [
        "천안시 동남구",
        "천안시 서북구",
        "공주시",
        "보령시",
        "아산시",
        "서산시",
        "논산시",
        "계룡시",
        "당진시",
        "금산군",
        "부여군",
        "서천군",
        "청양군",
        "홍성군",
        "예산군",
        "태안군",
      ],
      전라북도: [
        "전주시 완산구",
        "전주시 덕진구",
        "군산시",
        "익산시",
        "정읍시",
        "남원시",
        "김제시",
        "완주군",
        "진안군",
        "무주군",
        "장수군",
        "임실군",
        "순창군",
        "고창군",
        "부안군",
      ],
      전라남도: [
        "목포시",
        "여수시",
        "순천시",
        "나주시",
        "광양시",
        "담양군",
        "곡성군",
        "구례군",
        "고흥군",
        "보성군",
        "화순군",
        "장흥군",
        "강진군",
        "해남군",
        "영암군",
        "무안군",
        "함평군",
        "영광군",
        "장성군",
        "완도군",
        "진도군",
        "신안군",
      ],
      경상북도: [
        "포항시 남구",
        "포항시 북구",
        "경주시",
        "김천시",
        "안동시",
        "구미시",
        "영주시",
        "영천시",
        "상주시",
        "문경시",
        "경산시",
        "의성군",
        "청송군",
        "영양군",
        "영덕군",
        "청도군",
        "고령군",
        "성주군",
        "칠곡군",
        "예천군",
        "봉화군",
        "울진군",
        "울릉군",
      ],
      경상남도: [
        "창원시 의창구",
        "창원시 성산구",
        "창원시 마산합포구",
        "창원시 마산회원구",
        "창원시 진해구",
        "진주시",
        "통영시",
        "사천시",
        "김해시",
        "밀양시",
        "거제시",
        "양산시",
        "의령군",
        "함안군",
        "창녕군",
        "고성군",
        "남해군",
        "하동군",
        "산청군",
        "함양군",
        "거창군",
        "합천군",
      ],
      제주도: ["제주시", "서귀포시"],
    });

    const banks = ref([
      "한국은행",
      "KB국민은행",
      "신한은행",
      "우리은행",
      "하나은행",
      "SC제일은행",
      "한국씨티은행",
      "한국산업은행",
      "중소기업은행",
      "한국수출입은행",
      "NH농협은행",
      "수협은행",
      "대구은행",
      "부산은행",
      "경남은행",
      "광주은행",
      "전북은행",
      "제주은행",
    ]);
    return {
      cities,
      districts,
      banks,
    };
  },
  // watch: {
  //   selectedCity: function (newCity) {
  //     // 도시가 변경되면 해당 도시에 대한 구 목록을 업데이트합니다.
  //     this.selectedDistrict = null; // 선택된 구 초기화
  //     this.districts[this.selectedCity] = districts.value[newCity];
  //   },
  // },
  data() {
    return {
      keyword: "서울시 종로구 한국은행",
      selectedCity: "서울시",
      selectedDistrict: "종로구",
      selectedBank: "한국은행",
      map: null,
      markers: [],
      infowindow: new kakao.maps.InfoWindow({ zIndex: 1 }),
      ps: new kakao.maps.services.Places(),
    };
  },
  mounted() {
    this.initMap();
    this.searchPlaces();
  },
  methods: {
    initMap() {
      const mapContainer = document.querySelector("#map");
      const mapOption = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3,
      };
      this.map = new kakao.maps.Map(mapContainer, mapOption);
    },
    searchPlaces() {
      const searchQuery = `${this.selectedCity} ${this.selectedDistrict} ${this.selectedBank}`;
      this.keyword = searchQuery;
      console.log(searchQuery);
      this.ps.keywordSearch(this.keyword, this.placesSearchCB);
    },
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.");
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert("검색 결과 중 오류가 발생했습니다.");
      }
    },
    displayPlaces(places) {
      const listEl = document.getElementById("placesList");
      const bounds = new kakao.maps.LatLngBounds();
      this.removeAllChildNodes(listEl);
      this.removeMarker();

      places.forEach((place, index) => {
        const placePosition = new kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, index);
        const itemEl = this.getListItem(index, place);
        bounds.extend(placePosition);

        this.attachInfoWindow(marker, place.place_name, itemEl);
        listEl.appendChild(itemEl);
      });

      this.map.setBounds(bounds);
    },
    addMarker(position, idx) {
      const imageSrc =
        "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
      const imageSize = new kakao.maps.Size(36, 37);
      const imgOptions = {
        spriteSize: new kakao.maps.Size(36, 691),
        spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10),
        offset: new kakao.maps.Point(13, 37),
      };
      const markerImage = new kakao.maps.MarkerImage(
        imageSrc,
        imageSize,
        imgOptions
      );
      const marker = new kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.markers.push(marker);

      return marker;
    },
    attachInfoWindow(marker, title, itemEl) {
      kakao.maps.event.addListener(marker, "mouseover", () => {
        this.displayInfowindow(marker, title);
      });

      kakao.maps.event.addListener(marker, "mouseout", () => {
        this.infowindow.close();
      });

      itemEl.onmouseover = () => {
        this.displayInfowindow(marker, title);
      };

      itemEl.onmouseout = () => {
        this.infowindow.close();
      };
    },
    displayInfowindow(marker, title) {
      const content = '<div style="padding:5px;z-index:1;">' + title + "</div>";
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    removeMarker() {
      this.markers.forEach((marker) => {
        marker.setMap(null);
      });
      this.markers = [];
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById("pagination");
      const fragment = document.createDocumentFragment();

      while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild(paginationEl.lastChild);
      }

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement("a");
        el.href = "#";
        el.innerHTML = i;

        if (i === pagination.current) {
          el.className = "on";
        } else {
          el.onclick = () => {
            pagination.gotoPage(i);
          };
        }

        fragment.appendChild(el);
      }

      paginationEl.appendChild(fragment);
    },
    getListItem(index, place) {
      const el = document.createElement("li");
      let itemStr =
        '<span class="markerbg marker_' +
        (index + 1) +
        '"></span>' +
        '<div class="info">' +
        "<h5>" +
        place.place_name +
        "</h5>";

      if (place.road_address_name) {
        itemStr +=
          "<span>" +
          place.road_address_name +
          "</span>" +
          '<span class="jibun gray">' +
          place.address_name +
          "</span>";
      } else {
        itemStr += "<span>" + place.address_name + "</span>";
      }

      itemStr += '<span class="tel">' + place.phone + "</span>" + "</div>";

      el.innerHTML = itemStr;
      el.className = "item";

      return el;
    },
    removeAllChildNodes(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    },
  },
};
</script>

<style scoped>
.map-wrap {
  position: relative;
  width: 100%;
  height: 500px;
}

.bg-white {
  background: #fff;
}

.option {
  text-align: center;
}

.option p {
  margin: 10px 0;
}

.option button {
  margin-left: 5px;
}

#placesList li {
  list-style: none;
}

#placesList .item {
  position: relative;
  border-bottom: 1px solid #888;
  overflow: hidden;
  cursor: pointer;
  min-height: 65px;
}

#placesList .item span {
  display: block;
  margin-top: 4px;
}

#placesList .item h5,
#placesList .item .info {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

#placesList .item .info {
  padding: 10px 0 10px 55px;
}

#placesList .info .gray {
  color: #8a8a8a;
}

#placesList .info .jibun {
  padding-left: 26px;
  background: url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png)
    no-repeat;
}

#placesList .info .tel {
  color: #009900;
}

#placesList .item .markerbg {
  float: left;
  position: absolute;
  width: 36px;
  height: 37px;
  margin: 10px 0 0 10px;
  background: url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png)
    no-repeat;
}

#placesList .item .marker_1 {
  background-position: 0 -10px;
}

#placesList .item .marker_2 {
  background-position: 0 -56px;
}

#placesList .item .marker_3 {
  background-position: 0 -102px;
}

#placesList .item .marker_4 {
  background-position: 0 -148px;
}

#placesList .item .marker_5 {
  background-position: 0 -194px;
}

#placesList .item .marker_6 {
  background-position: 0 -240px;
}

#placesList .item .marker_7 {
  background-position: 0 -286px;
}

#placesList .item .marker_8 {
  background-position: 0 -332px;
}

#placesList .item .marker_9 {
  background-position: 0 -378px;
}

#placesList .item .marker_10 {
  background-position: 0 -423px;
}

#placesList .item .marker_11 {
  background-position: 0 -470px;
}

#placesList .item .marker_12 {
  background-position: 0 -516px;
}

#placesList .item .marker_13 {
  background-position: 0 -562px;
}

#placesList .item .marker_14 {
  background-position: 0 -608px;
}

#placesList .item .marker_15 {
  background-position: 0 -654px;
}

#pagination {
  margin: 10px auto;
  text-align: center;
}

#pagination a {
  display: inline-block;
  margin-right: 10px;
}

#pagination .on {
  font-weight: bold;
  cursor: default;
  color: #777;
}
</style>
