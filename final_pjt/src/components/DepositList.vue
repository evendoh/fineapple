<template>
  <div>
    &nbsp;
  </div>
  <h1>예금 리스트</h1>
  <div>
    &nbsp;
  </div>
    <table class="styled-table">
        <thead>
      <tr>
        <th>ID</th>
        <th>Bank</th>
        <th>Product</th>
        <th>6개월</th>
        <th>12개월</th>
        <th>24개월</th>
        <th>36개월</th>
      </tr>
    </thead>
  
      </table>
  
      
      <DepositListItem
        v-for="item in store.depositProducts"
        :key="item.id"
        :item="item"
      />
  
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import DepositListItem from '@/components/DepositListItem.vue';
  
  const store = useCounterStore();
  const item = ref([{
              "id": 1,
              "fin_prdt_cd": "WR0001B",
              "kor_co_nm": "우리은행",
              "fin_prdt_nm": "WON플러스예금",
              "etc_note": "- 가입기간: 1~36개월\n- 최소가입금액: 1만원 이상\n- 만기일을 일,월 단위로 자유롭게 선택 가능\n- 만기해지 시 신규일 당시 영업점과 인터넷 홈페이지에 고시된 계약기간별 금리 적용",
              "join_deny": 1,
              "join_member": "실명의 개인",
              "join_way": "인터넷,스마트폰,전화(텔레뱅킹)",
              "spcl_cnd": "해당사항 없음",
              "mtrt_int": "만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리",
              "max_limit": null
          },])
  const options = ref([{
              "id": 108,
              "fin_prdt_cd": "10-01-20-388-0002",
              "intr_rate_type_nm": "단리",
              "intr_rate": 3.9,
              "intr_rate2": 3.9,
              "save_trm": 6,
              "product": 37
          },])      
  </script>
  
  
  <style>
  h1{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
    .table-container {
      max-width: 1000px;
      margin: auto;
    }
  
    .styled-table {
      width: 100%;
      border-collapse: collapse;
      margin: auto;
      max-width: 1000px;
    }
  
    .styled-table tr {
      border-bottom: 1px solid #ddd;
    }
  
    .styled-table td {
      padding: 12px; /* 기본값 */
      text-align: left;
    }
  
    .styled-table td.label {
      font-weight: bold;
      width: 10%;
    }
  
    .styled-table td.bank {
      width: 20%;
    }
  
    .styled-table td.product {
      font-weight: bold;
      width: 30%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  
    .styled-table td.option1,
    .styled-table td.option2,
    .styled-table td.option3,
    .styled-table td.option4 {
      width: 10%;
    }
  
    .details-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
  
    .details-table td {
      padding: 12px; /* 조절된 값 */
      border-bottom: 1px solid #ddd;
      background-color: white;
    }
  
    .td1 {
      font-weight: bold;
      width: 25%;
    }
    .options {
      width: 40%;
      align-items: right;
    }
  </style>
  