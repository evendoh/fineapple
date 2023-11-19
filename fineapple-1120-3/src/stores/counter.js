import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  
  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`
    })
    .then((response) => {
      // console.log(response)
      articles.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const exchangeRates = ref([])
    // DRF에 환율 조회 요청을 보내는 action
  const getExchangeRates = function() {
    axios({
      method: 'get',
      url: `${API_URL}/exchange/`
    })
    .then((response) => {
      // console.log(response)
      exchangeRates.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const savingProducts = ref([])
  // DRF에 적금정보 조회 요청을 보내는 action
const getSavingProducts = function() {
  axios({
    method: 'get',
    url: `${API_URL}/financial/saving_products/`
  })
  .then((response) => {
    // console.log(response.data)
    savingProducts.value = response.data
    console.log(savingProducts.value)
  })
  .catch((error) => {
    console.log(error)
  })
}

const depositProducts = ref([])
// DRF에 예금정보 조회 요청을 보내는 action
const getDepositProducts = function() {
axios({
  method: 'get',
  url: `${API_URL}/financial/deposit_products/`
})
.then((response) => {
  // console.log(response.data)
  depositProducts.value = response.data
  console.log(depositProducts.value)
})
.catch((error) => {
  console.log(error)
})
}
  return { articles, exchangeRates, savingProducts, depositProducts, API_URL, getArticles, getExchangeRates, getSavingProducts, getDepositProducts }
}, { persist: true })