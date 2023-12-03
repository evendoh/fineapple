<template>
    <div>
    &nbsp;
  </div>
  <div>
    <h1>적금 리스트</h1>
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
    <SavingListItem
      v-for="item in store.savingProducts"
      :key="item.id"
      :item="item"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import SavingListItem from "@/components/SavingListItem.vue";

const store = useCounterStore();
console.log("saving :", store.savingProducts);
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
