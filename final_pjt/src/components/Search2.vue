<template>
  <form id="form" role="search">
    <input
      v-model="searchQuery"
      type="search"
      id="query"
      name="q"
      placeholder="은행명을 입력하세요"
      aria-label="은행 검색"
      @input="handleSearch"
    />

    <button @click="handleSearch">find</button>
  </form>
</template>

<script setup>
import { ref } from "vue";

const searchQuery = ref("");

const banks = ref({
  중앙은행: [{ 한국은행: "https://www.bok.or.kr/portal/main/main.do" }],
  시중은행: [
    { KB국민은행: "https://www.kbstar.com/" },
    { 신한은행: "https://www.shinhan.com/index.jsp" },
    { 우리은행: "https://www.wooribank.com/" },
    { 하나은행: "https://www.kebhana.com/" },
    { SC제일은행: "https://www.standardchartered.co.kr/np/kr/Intro.jsp" },
    { 한국씨티은행: "https://www.citibank.co.kr/ComMainCnts0100.act?ref=" },
  ],
  특수은행: [
    { 한국산업은행: "https://www.kdb.co.kr/index.jsp" },
    { 중소기업은행: "https://www.ibk.co.kr/" },
    { 한국수출입은행: "https://www.koreaexim.go.kr/index" },
    { NH농협은행: "https://www.nonghyup.com/main/psniMain.do" },
    { 수협은행: "https://www.suhyup-bank.com/" },
  ],
  지방은행: [
    { 대구은행: "https://www.dgb.co.kr/dgb_ebz_main.jsp" },
    { 부산은행: "https://www.busanbank.co.kr/ib20/mnu/BHP00001" },
    { 경남은행: "https://www.knbank.co.kr/ib20/mnu/BHP000000000001" },
    { 광주은행: "https://pib.kjbank.com/ib20/mnu/BPB0000000001" },
    { 전북은행: "https://www.jbbank.co.kr/" },
    { 제주은행: "https://www.e-jejubank.com/JeJuBankInfo.do" },
  ],
});

const handleSearch = () => {
  const query = searchQuery.trim();
  let found = false;

  // Iterate through categories
  for (const category in banks.value) {
    const banksInCategory = banks.value[category];

    // Check if the entered bank name exists in the current category
    const bankIndex = banksInCategory.findIndex((bank) =>
      Object.keys(bank)[0].includes(query)
    );

    if (bankIndex !== -1) {
      const bankInfo = banksInCategory[bankIndex];
      const bankURL = Object.values(bankInfo)[0];
      window.open(bankURL, "_blank");
      found = true;
      break;
    }
  }

  if (!found) {
    // Handle case when the entered bank name is not in the list
    alert("해당 은행을 찾을 수 없습니다.");
  }
};
</script>

<style scoped>
body {
  background-color: #1e4b4c;
  margin: 200px 40%;
}

form {
  background-color: white;
  width: 60%;
  height: 44px;
  margin-top: 100px;
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
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
