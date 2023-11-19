<template>
<div class='wrapper'>
  <div class='carousel'>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍎
      </div>
      <div class='carousel__item-body'>
        <p class='title'>spouting whale</p>
        <p>Unicode: U+1F433</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍎
      </div>
      <div class='carousel__item-body'>
        <p class='title'>whale</p>
        <p>Unicode: U+1F40B</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍎
      </div>
      <div class='carousel__item-body'>
        <p class='title'>dolphin</p>
        <p>Unicode: U+1F42C</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍎
      </div>
      <div class='carousel__item-body'>
        <p class='title'>fish</p>
        <p>Unicode: U+1F41F</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍏
      </div>
      <div class='carousel__item-body'>
        <p class='title'>tropical fish</p>
        <p>Unicode: U+1F420</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍏
      </div>
      <div class='carousel__item-body'>
        <p class='title'>blowfish</p>
        <p>Unicode: U+1F421</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍏
      </div>
      <div class='carousel__item-body'>
        <p class='title'>shark</p>
        <p>Unicode: U+1F988</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍏
      </div>
      <div class='carousel__item-body'>
        <p class='title'>octopus</p>
        <p>Unicode: U+1F419</p>
      </div>
    </div>
    <div class='carousel__item'>
      <div class='carousel__item-head'>
        🍏
      </div>
      <div class='carousel__item-body'>
        <p class='title'>spiral shell</p>
        <p>Unicode: U+1F41A</p>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>

</script>

<style scoped>
*, *::before, *::after {
  box-sizing: border-box;
}

body, .cd__main {
  font-family: "Work Sans", sans-serif;
  font-weight: 400;
  height: 100vh;
}

.wrapper {
  background: linear-gradient(60deg, #420285, #08BDBD);
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
}

.carousel {
  position: relative;
  width: 100%;
  max-width: 1000px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.carousel__item {
  display: flex;
  align-items: center;
  position: absolute;
  width: 100%;
  padding: 0 12px;
  opacity: 0;
  filter: drop-shadow(0 2px 2px #555);
  will-change: transform, opacity;
  -webkit-animation: carousel-animate-vertical 27s linear infinite;
          animation: carousel-animate-vertical 27s linear infinite;
}

.carousel__item:nth-child(1) {
  -webkit-animation-delay: calc(3s * -1);
          animation-delay: calc(3s * -1);
}

.carousel__item:nth-child(2) {
  -webkit-animation-delay: calc(3s * 0);
          animation-delay: calc(3s * 0);
}

.carousel__item:nth-child(3) {
  -webkit-animation-delay: calc(3s * 1);
          animation-delay: calc(3s * 1);
}

.carousel__item:nth-child(4) {
  -webkit-animation-delay: calc(3s * 2);
          animation-delay: calc(3s * 2);
}

.carousel__item:nth-child(5) {
  -webkit-animation-delay: calc(3s * 3);
          animation-delay: calc(3s * 3);
}

.carousel__item:nth-child(6) {
  -webkit-animation-delay: calc(3s * 4);
          animation-delay: calc(3s * 4);
}

.carousel__item:nth-child(7) {
  -webkit-animation-delay: calc(3s * 5);
          animation-delay: calc(3s * 5);
}

.carousel__item:nth-child(8) {
  -webkit-animation-delay: calc(3s * 6);
          animation-delay: calc(3s * 6);
}

.carousel__item:last-child {
  -webkit-animation-delay: calc(-3s * 2);
          animation-delay: calc(-3s * 2);
}

.carousel__item-head {
  border-radius: 50%;
  background-color: #d7f7fc;
  width: 90px;
  height: 90px;
  padding: 14px;
  position: relative;
  margin-right: -45px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 50px;
}

.carousel__item-body {
  width: 100%;
  background-color: #fff;
  border-radius: 8px;
  padding: 16px 20px 16px 70px;
}

.title {
  text-transform: uppercase;
  font-size: 20px;
  margin-top: 10px;
}

@-webkit-keyframes carousel-animate-vertical {
  0% {
    transform: translateY(100%) scale(0.5);
    opacity: 0;
    visibility: hidden;
  }
  3%, 11.1111111111% {
    transform: translateY(100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  14.1111111111%, 22.2222222222% {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
  25.2222222222%, 33.3333333333% {
    transform: translateY(-100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  36.3333333333% {
    transform: translateY(-100%) scale(0.5);
    opacity: 0;
    visibility: visible;
  }
  100% {
    transform: translateY(-100%) scale(0.5);
    opacity: 0;
    visibility: hidden;
  }
}

@keyframes carousel-animate-vertical {
  0% {
    transform: translateY(100%) scale(0.5);
    opacity: 0;
    visibility: hidden;
  }
  3%, 11.1111111111% {
    transform: translateY(100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  14.1111111111%, 22.2222222222% {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
  25.2222222222%, 33.3333333333% {
    transform: translateY(-100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  36.3333333333% {
    transform: translateY(-100%) scale(0.5);
    opacity: 0;
    visibility: visible;
  }
  100% {
    transform: translateY(-100%) scale(0.5);
    opacity: 0;
    visibility: hidden;
  }
}
</style>

