<template>
    <form id="form" role="search">
  <input type="search" id="query" name="q"
   placeholder="금융상품 검색"
   aria-label="Search through site content">
  <button>Find</button>
</form>
</template>

<script setup>
// const f = document.getElementById('form');
// const q = document.getElementById('query');
// const google = 'https://www.google.com/search?q=site%3A+';
// const site = 'pagedart.com';

// function submitted(event) {
//   event.preventDefault();
//   const url = google + site + '+' + q.value;
//   const win = window.open(url, '_blank');
//   win.focus();
// }

// f.addEventListener('submit', submitted);
</script>

<style scoped>
        body {
        background-color: #1E4B4C;
        margin: 200px 40%;
      }

      form {
        background-color: white;
        width: 60%;
        height: 44px;
        margin-top: 100px;
        border-radius: 5px;
        display:flex;
        flex-direction:row;
        align-items:center;
      }

      input {
        all: unset;
        font: 16px system-ui;
        color: black;
        height: 100%;
        width: 100%;
        padding: 6px 10px;
      }

      ::placeholder {
        color: black;
        opacity: 0.7; 
      }

      svg {
        color: #fff;
        fill: currentColor;
        width: 24px;
        height: 24px;
        padding: 10px;
      }

      button {
        all: unset;
        cursor: pointer;
        width: 44px;
        height: 44px;
      }
</style>