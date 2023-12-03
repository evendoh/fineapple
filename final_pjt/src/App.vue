<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink
          :to="{ path: '/', exact: true }"
          class="nav-button"
          id="fineapple"
        >
          FineApple🍎
        </RouterLink>
        <RouterLink to="/financialproducts" class="nav-button">
          예적금비교
        </RouterLink>
        <RouterLink to="/bankmap" class="nav-button"> 은행 지도 </RouterLink>
        <RouterLink to="/exchange" class="nav-button"> 환율 </RouterLink>
        <RouterLink to="/article" class="nav-button"> 게시판 </RouterLink>
        <RouterLink to="/product-suggest" class="nav-button"
          >금융 상품 추천</RouterLink
        >
        <div v-if="!store.isLogin" class="nav-button" id="auth">
          <RouterLink :to="{ name: 'SignUpView' }" class="nav-button"
            >회원가입</RouterLink
          >
          |
          <RouterLink :to="{ name: 'LogInView' }" class="nav-button"
            >로그인</RouterLink
          >
        </div>
        <div v-else class="nav-button" id="auth">
          <RouterLink :to="{ name: 'ProfileView' }" class="nav-button"
            >프로필</RouterLink
          >
          |
          <button @click="logOut" class="nav-button btn">로그아웃</button>
        </div>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();

const logOut = store.logOut;
</script>

<style>
template{
  /* font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; */
}

#fineapple {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 600;
}
#auth {
  font-weight: lighter;
  font-size: x-small;
}
.wrapper {
  width: 70%;
  display: flex;
  text-align: center;
  flex-direction: space-between;
}
header {
  line-height: 1.5;
  max-height: 100vh;
  background-color: rgb(0, 75, 76);
  width: 100%;
  padding: 1rem 0;
}
nav {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* font-family: "Courier New", Courier, monospace; */
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.auth-buttons {
  display: flex;
  align-items: center;
}

.nav-button {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  transition: background-color 0.3s;
}

.nav-button:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
}

@media (min-width: 768px) {
  .nav-button {
    font-size: 1.2rem;
  }
}

@media (min-width: 1024px) {
  header {
    padding-right: calc(var(--section-gap) / 2);
  }

  nav {
    padding: 0;
  }

  .auth-buttons {
    font-size: 1rem;
  }

  .nav-button {
    font-size: 1rem;
  }
}
</style>