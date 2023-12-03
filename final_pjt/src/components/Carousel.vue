<template>
  <div class="wrapper">
    <div class="carousel">
      <div
        class="carousel__item"
        v-for="(item, index) in items"
        :key="item.id"
        :style="{ 'animation-delay': `${3 * (index - 2)}s` }"
      >
        <div class="carousel__item-body">
          <div class="carousel__item-head">
            <div class="emoji">
              {{ currentEmoji(item.id) }}
            </div>
            <div class="percent">
              {{ likeRatio(item.id).toFixed(0) + "%" }}
            </div>
          </div>
          <div class="carousel__item-info" >
            <div @click="moveProduct">
            <p class="title">{{ item.kor_co_nm }}</p>
            <p>
              {{ item.fin_prdt_nm }}
            </p>
          </div>
            <div class="like-dislike-ratio">
              <div
                class="like-ratio"
                :style="{ width: likeRatio(item.id) + '%' }"
              ></div>
              <div
                class="dislike-ratio"
                :style="{ width: dislikeRatio(item.id) + '%' }"
              ></div>
            </div>
            <div class="like-dislike-buttons">
              <button @click="() => like(item.id)" class="fine-label">
                Fine <br /><strong>{{ getLikeCount(item.id) }}</strong>
              </button>
              <button @click="() => dislike(item.id)" class="poor-label">
                Poor <br /><strong>{{ getDislikeCount(item.id) }}</strong>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useCounterStore();
onMounted(() => {
  store.getDepositProducts();
  store.getSavingProducts();
});

// 금융 상품들을 랜덤으로 출력
const items = ref([]);
items.value = [...store.depositProducts, ...store.savingProducts];
items.value.sort(() => Math.random() - 0.5);

// 더미 데이터를 반영하는 대신 fine과 poor를 랜덤 생성
const likeCount = ref({});
const dislikeCount = ref({});

const getRandomCount = () => Math.floor(Math.random() * 1001);
[...store.depositProducts, ...store.savingProducts].forEach((item) => {
  likeCount.value[item.id] = getRandomCount();
  dislikeCount.value[item.id] = getRandomCount();
});


console.log(likeCount.value);
console.log(dislikeCount.value);

const itemLikes = ref({});
const itemDislikes = ref({});

items.value.forEach((item) => {
  itemLikes.value[item.id] = ref(likeCount.value[item.id] || 0);
  itemDislikes.value[item.id] = ref(dislikeCount.value[item.id] || 0);
});

// 각 아이템의 value를 증가시키는 함수 정의
const like = (itemId) => {
  if (!likeCount.value[itemId]) {
    likeCount.value[itemId] = 0;
  }
  likeCount.value[itemId]++;
};

const dislike = (itemId) => {
  if (!dislikeCount.value[itemId]) {
    dislikeCount.value[itemId] = 0;
  }
  dislikeCount.value[itemId]++;
};

const getLikeCount = (itemId) => likeCount.value[itemId] || 0;
const getDislikeCount = (itemId) => dislikeCount.value[itemId] || 0;

// like count를 가져와서 비율 계산하는 함수
const likeRatio = (itemId) => {
  const likes = getLikeCount(itemId);
  const dislikes = getDislikeCount(itemId);
  return (likes / (likes + dislikes)) * 100 || 0;
};

const dislikeRatio = (itemId) => {
  const likes = getLikeCount(itemId);
  const dislikes = getDislikeCount(itemId);
  return (dislikes / (likes + dislikes)) * 100 || 0;
};

const currentEmoji = (itemId) => {
  return likeRatio(itemId) > dislikeRatio(itemId) ? "🍎" : "🍏";
};

const moveProduct = () => {
  router.push('/financialproducts');
}; 
</script>

<style scoped>
.wrapper {
  height: 40vh;
  margin-left: 20%;
  display: flex;
  justify-content: center;
  /* align-items: center;  */
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
  padding: 0 2px;
  opacity: 0;
  filter: drop-shadow(0 2px 2px #555);
  will-change: transform, opacity;
  -webkit-animation: carousel-animate-vertical 27s linear infinite;
  animation: carousel-animate-vertical 27s linear infinite;
}
.carousel__item:nth-child(1),
.carousel__item:nth-child(2),
.carousel__item:nth-child(3),
.carousel__item:nth-child(4),
.carousel__item:nth-child(5),
.carousel__item:nth-child(6),
.carousel__item:nth-child(7),
.carousel__item:nth-child(8),
.carousel__item:last-child {
  -webkit-animation-delay: calc(3s * -1);
  animation-delay: calc(3s * -1);
}

.carousel__item:nth-child(2),
.carousel__item:nth-child(3),
.carousel__item:nth-child(4),
.carousel__item:nth-child(5),
.carousel__item:nth-child(6),
.carousel__item:nth-child(7),
.carousel__item:nth-child(8),
.carousel__item:last-child {
  -webkit-animation-delay: calc(3s * -1 + 3s);
  animation-delay: calc(3s * -1 + 3s);
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
}

.emoji {
  font-size: 50px;
}
.percent {
  font-size: 15px;
  font-weight: bolder;
}

.carousel__item-info {
  width: 100%;
  background-color: #fff;
  border-radius: 8px;
  padding: 16px 20px 16px 70px;
}

.title {
  text-transform: uppercase;
  font-size: 20px;
  margin-top: 10px;
  font-weight: 600;
}

.like-dislike-buttons {
  display: flex;
  flex-direction: row;
  gap: 8px;
}

.like-button,
.dislike-button {
  font-size: 30px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
}

.like-dislike-ratio {
  display: flex;
  align-items: center;
  margin-top: 8px;
}

.like-ratio,
.dislike-ratio {
  height: 8px;
  border-radius: 4px;
}

.like-ratio {
  background-color: #f44336; /* 빨간색 */
}

.dislike-ratio {
  background-color: rgb(0, 75, 76); /* 초록색 */
}

.label {
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
}

.fine-label,
.poor-label {
  text-align: center;
  font-size: 12px;
  width: 48%;
  background-color: white;
  border: none;
}

.fine-label {
  color: #f44336; /* 빨간색 */
}

.poor-label {
  color: rgb(0, 75, 76); /* 초록색 */
}

@-webkit-keyframes carousel-animate-vertical {
  0% {
    transform: translateY(100%) scale(0.5);
    opacity: 0;
    visibility: hidden;
  }
  3%,
  11.1111111111% {
    transform: translateY(100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  14.1111111111%,
  22.2222222222% {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
  25.2222222222%,
  33.3333333333% {
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
  3%,
  11.1111111111% {
    transform: translateY(100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  14.1111111111%,
  22.2222222222% {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
  25.2222222222%,
  33.3333333333% {
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
.carousel__item-body {
  display: flex;
  width: 100%;
  justify-content: space-between;
}
</style>
<!-- 
<template>
  <div class="wrapper">
    <div class="carousel">
      <div
        class="carousel__item"
        v-for="(item, index) in items"
        :key="item.id"
        :style="{ 'animation-delay': `${3 * (index - 2)}s` }"
      >
        <div class="carousel__item-body">
          <div class="carousel__item-head">{{ currentEmoji(item.id) }}</div>
          <div class="carousel__item-info">
            <p class="title">{{ item.kor_co_nm }}</p>
            <p>{{ item.fin_prdt_nm }}</p>
            <div class="like-dislike-ratio">
              <div
                class="like-ratio"
                :style="{ width: likeRatio(item.id) + '%' }"
              ></div>
              <div
                class="dislike-ratio"
                :style="{ width: dislikeRatio(item.id) + '%' }"
              ></div>
            </div>
            <div class="like-dislike-buttons">
              <button @click="() => like(item.id)" class="fine-label">
                Fine
              </button>
              <button @click="() => dislike(item.id)" class="poor-label">
                Poor
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
onMounted(() => {
  store.getDepositProducts();
  store.getSavingProducts();
});

const items = ref([]);
items.value = [...store.depositProducts, ...store.savingProducts];
items.value.sort(() => Math.random() - 0.5);

const likeCount = ref({});
const dislikeCount = ref({});

const like = (itemId) => {
  if (!likeCount.value[itemId]) {
    likeCount.value[itemId] = 0;
  }
  likeCount.value[itemId]++;
};

const dislike = (itemId) => {
  if (!dislikeCount.value[itemId]) {
    dislikeCount.value[itemId] = 0;
  }
  dislikeCount.value[itemId]++;
};

const getLikeCount = (itemId) => likeCount.value[itemId] || 0;
const getDislikeCount = (itemId) => dislikeCount.value[itemId] || 0;

const likeRatio = (itemId) => {
  const likes = getLikeCount(itemId);
  const dislikes = getDislikeCount(itemId);
  return (likes / (likes + dislikes)) * 100 || 0;
};

const dislikeRatio = (itemId) => {
  const likes = getLikeCount(itemId);
  const dislikes = getDislikeCount(itemId);
  return (dislikes / (likes + dislikes)) * 100 || 0;
};

const currentEmoji = (itemId) => {
  return likeRatio(itemId) > dislikeRatio(itemId) ? "🍎" : "🍏";
};
</script>

<style scoped>
.wrapper {
  height: 40vh;
  margin-left: 20%;

  display: flex;
  justify-content: center;
  /* align-items: center;  */
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
  padding: 0 2px;
  opacity: 0;
  filter: drop-shadow(0 2px 2px #555);
  will-change: transform, opacity;
  -webkit-animation: carousel-animate-vertical 27s linear infinite;
  animation: carousel-animate-vertical 27s linear infinite;
}
.carousel__item:nth-child(1),
.carousel__item:nth-child(2),
.carousel__item:nth-child(3),
.carousel__item:nth-child(4),
.carousel__item:nth-child(5),
.carousel__item:nth-child(6),
.carousel__item:nth-child(7),
.carousel__item:nth-child(8),
.carousel__item:last-child {
  -webkit-animation-delay: calc(3s * -1);
  animation-delay: calc(3s * -1);
}

.carousel__item:nth-child(2),
.carousel__item:nth-child(3),
.carousel__item:nth-child(4),
.carousel__item:nth-child(5),
.carousel__item:nth-child(6),
.carousel__item:nth-child(7),
.carousel__item:nth-child(8),
.carousel__item:last-child {
  -webkit-animation-delay: calc(3s * -1 + 3s);
  animation-delay: calc(3s * -1 + 3s);
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

.carousel__item-info {
  width: 100%;
  background-color: #fff;
  border-radius: 8px;
  padding: 16px 20px 16px 70px;
}

.title {
  text-transform: uppercase;
  font-size: 20px;
  margin-top: 10px;
  font-weight: 600;
}

.like-dislike-buttons {
  display: flex;
  flex-direction: row;
  gap: 8px;
}

.like-button,
.dislike-button {
  font-size: 30px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
}

.like-dislike-ratio {
  display: flex;
  align-items: center;
  margin-top: 8px;
}

.like-ratio,
.dislike-ratio {
  height: 8px;
  border-radius: 4px;
}

.like-ratio {
  background-color: #f44336; /* 빨간색 */
}

.dislike-ratio {
  background-color: rgb(0, 75, 76); /* 초록색 */
}

.label {
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
}

.fine-label,
.poor-label {
  text-align: center;
  font-size: 12px;
  width: 48%;
  background-color: white;
  border: none;
}

.fine-label {
  color: #f44336; /* 빨간색 */
}

.poor-label {
  color: rgb(0, 75, 76); /* 초록색 */
}

@-webkit-keyframes carousel-animate-vertical {
  0% {
    transform: translateY(100%) scale(0.5);
    opacity: 0;
    visibility: hidden;
  }
  3%,
  11.1111111111% {
    transform: translateY(100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  14.1111111111%,
  22.2222222222% {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
  25.2222222222%,
  33.3333333333% {
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
  3%,
  11.1111111111% {
    transform: translateY(100%) scale(0.7);
    opacity: 0.4;
    visibility: visible;
  }
  14.1111111111%,
  22.2222222222% {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
  25.2222222222%,
  33.3333333333% {
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
.carousel__item-body {
  display: flex;
  width: 100%;
  justify-content: space-between;
}
</style> -->
