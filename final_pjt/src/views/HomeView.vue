<template>
  <main>
    <div class="banner">
      <router-link class="banner__logo" to="/" tag="div">
        <Logo />
      </router-link>
      <div class="mbti">
        <p class="mbti__title">나의 금융 MBTI</p>
        <RouterLink to="/testmain" >
          <p>검사하러 가기↗️↗️↗️</p>
        </RouterLink>
      </div>
    </div>
    <div class="space200"></div>
    <div class="carousel">
      <Carousel />
    </div>
    <footer class="footer">
      <p>© 2023 FineApple. All rights reserved.</p>
    </footer>
  </main>
</template>

<script setup>
import Carousel from "@/components/Carousel.vue";
import Search from "@/components/Search.vue";
import Logo from "@/components/Logo.vue";
</script>

<style>
.banner {
  width: 100%;
  height: 20%;
  background-color: rgb(0, 75, 76);
  display: flex;
  justify-content: space-between;
  position: relative;
  z-index: 1;
}

.banner__logo {
  width: 50%;
}

.mbti {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: small; /* Adjust the font size to make it smaller */
  font-weight: lighter;
  width: 50%;
}

.mbti > a {
  text-decoration: none;
  color: white;
}

.mbti__title {
  margin: 0; /* Remove default margin for the 'p' elements */
  font-size: 1.5rem;
  color: white;
  font-weight: bold;
}

.mbti p {
  margin: 0; /* Remove default margin for the 'p' elements */
  font-size: 1.5rem;
  font-weight: bold;
}

.mbti p:first-child {
  margin-top: 2rem;
}
.carousel {
  position: relative;
  width: 120%;
  height: 20%;
  max-width: 1000px;
  margin: 10px auto; /* 수직 가운데 정렬을 위해 margin을 auto로 설정 */
  z-index: 0;
}

.space200 {
  height: 100px;
}

.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f0f0f0;
  /* 회색 배경색 지정 / padding: 3px; / 상하좌우 여백 지정 / text-align: center; /
  텍스트 가운데 정렬 */
  height: 10%;
}
</style>
