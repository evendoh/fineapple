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
      <input type="submit" value="찾기" />
      <!-- <input type="file" accept=".csv, appliction/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" /> -->
    </form>
  </div>
  <div class="space"></div>
  <div id="map" style="width:750px;height:350px;"></div>
    </template>
    
    
    <script setup>
    import { onMounted } from 'vue';
    onMounted(() => {
    var mapContainer = document.querySelector('#map') // 지도를 표시할 div 
    var mapOption = {
        center: new kakao.maps.LatLng(37.56588, 126.97837), // 지도의 중심좌표
        level: 3, // 지도의 확대 레벨
        mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
        }; 
    var map = new kakao.maps.Map(mapContainer, mapOption); 
    })
    // // 지도를 생성한다 
    
    // // 지도 중심 좌표 변화 이벤트를 등록한다
    // kakao.maps.event.addListener(map, 'center_changed', function () {
    //     console.log('지도의 중심 좌표는 ' + map.getCenter().toString() +' 입니다.');
    // });
    
    // // 지도 확대 레벨 변화 이벤트를 등록한다
    // kakao.maps.event.addListener(map, 'zoom_changed', function () {
    //     console.log('지도의 현재 확대레벨은 ' + map.getLevel() +'레벨 입니다.');
    // });
    
    // 지도에 마커를 생성하고 표시한다
    // var marker = new kakao.maps.Marker({
    //     position: new kakao.maps.LatLng(37.56588, 126.97837), // 마커의 좌표
    //     draggable : true, // 마커를 드래그 가능하도록 설정한다
    //     map: map // 마커를 표시할 지도 객체
    // });
    
    </script>

    <style>
  .space{
    height: 50px;
  }
  .search {
    margin-left: 100px;
  }
  #map {
    margin-left: 100px;
  }
  </style>

