<template>
  <div class="box">
    <div class="flex">
      <p class="author">
        {{ article.user.name }}
        {{ '🍎'.repeat(Number(article.likes_count))}}
      </p>

      <div class="detail">
        <p>
          조회: {{ article.views }} / 댓글: {{ article.comments_count }}
          / 작성:
          {{ formatDate(article.created_at) }}
        </p>
      </div>
    </div>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }">
      <p class="title">
        {{ article.title }}
      </p>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  article: Object,
});

const formatDate = (dateString) => {
  const options = { year: "numeric", month: "long", day: "numeric" };
  return new Date(dateString).toLocaleDateString("ko-KR", options);
};
</script>

<style scoped>
.box {
  border: 1px solid;
  border-radius: 2px;
  padding: 10px;
  margin-bottom: 10px;
}

.title {
  font-weight: bold;
  margin-left: 15%;
}

.content {
  color: #333; /* 내용 글자색을 어두운 색으로 설정 */
}
.detail {
  font-size: 10px;
  display: flex;
}
.author {
  font-size: 15px;
  display: flex;
}
.flex {
  display: flex;
  justify-content: space-around;
}
</style>
