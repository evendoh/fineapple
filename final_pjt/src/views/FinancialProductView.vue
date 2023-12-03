
<template>
  <div>
    &nbsp;
  </div>
  <div class="container">
    <h1>내 조건에 맞는 상품 찾기</h1>
    <div class="box-container">
      <div class="deposit-box">
        <RouterLink :to="{ name: 'DepositList' }">
          <button class="button">예금 상품</button>
        </RouterLink>
      </div>
      <div class="saving-box">
        <RouterLink :to="{ name: 'SavingList' }">
          <button class="button">적금 상품</button>
        </RouterLink>
      </div>
    </div>
    <form action="" class="center" @submit.prevent="handleSubmit">
      <div class="select-wrapper">
        <select name="은행" id="bank" v-model="bank">
          <option value="국민은행">국민은행</option>
          <option value="우리은행">우리은행</option>
          <option value="신한은행">신한은행</option>
          <option value="하나은행">하나은행</option>
          <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
          <option value="한국산업은행">한국산업은행</option>
          <option value="농협은행주식회사">농협은행주식회사</option>
          <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
          <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
          <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
          <option value="중소기업은행">중소기업은행</option>
          <option value="부산은행">부산은행</option>
          <option value="대구은행">대구은행</option>
          <option value="광주은행">광주은행</option>
          <option value="경남은행">경남은행</option>
          <option value="전북은행">전북은행</option>
          <option value="제주은행">제주은행</option>
          <option value="수협은행">수협은행</option>
        </select>
      </div>
      <div class="select-wrapper">
        <select name="예치기간" id="term" v-model="term">
          <option value="6">6개월</option>
          <option value="12">12개월</option>
          <option value="24">24개월</option>
          <option value="36">36개월</option>
        </select>
      </div>
      <button type="submit" class="button">찾기</button>
    </form>
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
    <div class="table-container" v-for="item in filteredDepositList">
      <table class="styled-table">
        <tr>
          <td class="label">
            {{ item.id }}
          </td>
          <td class="bank">
            {{ item.kor_co_nm }}
          </td>
          <td class="product">
            <span @click="toggleDetails">{{ item.fin_prdt_nm }}</span>
          </td>

          <td class="option1">
            <p>
              {{
                options
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 6)[0]
                  ? options
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 6)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
          <td class="option2">
            <p>
              {{
                options
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 12)[0]
                  ? options
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 12)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
          <td class="option3">
            <p>
              {{
                options
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 24)[0]
                  ? options
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 24)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
          <td class="option4">
            <p>
              {{
                options
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 36)[0]
                  ? options
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 36)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
        </tr>
        <tr v-if="showDetails">
          <td colspan="12">
            <table class="details-table">
              <tr>
                <td class="td1">금융상품설명</td>
                <td>{{ item.etc_note }}</td>
              </tr>
              <tr>
                <td class="td1">가입제한</td>
                <td>
                  <span v-if="item.join_deny === 1">제한 없음</span>
                  <span v-else-if="item.join_deny === 2">서민전용</span>
                  <span v-else-if="item.join_deny === 3">일부제한</span>
                </td>
              </tr>
              <tr>
                <td class="td1">가입대상</td>
                <td>{{ item.join_member }}</td>
              </tr>
              <tr>
                <td class="td1">가입방법</td>
                <td>{{ item.join_way }}</td>
              </tr>
              <tr>
                <td class="td1">우대조건</td>
                <td>{{ item.spcl_cnd }}</td>
              </tr>
              <tr>
                <td class="td1">만기 후 이자율</td>
                <td>{{ item.mtrt_int }}</td>
              </tr>
              <tr>
                <td class="td1">최고한도</td>
                <td>{{ item.max_limit }}</td>
              </tr>
            </table>
            <button @click="handleButtonClick">
              {{ showDetails2 ? "해지하기" : "가입하기" }}
            </button>
          </td>
        </tr>
      </table>

      <table class="styled-table">
        <tr v-for="item in filteredSavingList">
          <td class="label">
            {{ item.id }}
          </td>
          <td class="bank">
            {{ item.kor_co_nm }}
          </td>
          <td class="product">
            <span @click="toggleDetails">{{ item.fin_prdt_nm }}</span>
          </td>

          <td class="option1">
            <p>
              {{
                options2
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 6)[0]
                  ? options2
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 6)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
          <td class="option2">
            <p>
              {{
                options2
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 12)[0]
                  ? options2
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 12)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
          <td class="option3">
            <p>
              {{
                options2
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 24)[0]
                  ? options2
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 24)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
          <td class="option4">
            <p>
              {{
                options2
                  .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                  .filter((option) => option.save_trm === 36)[0]
                  ? options2
                      .filter(
                        (option) => option.fin_prdt_cd === item.fin_prdt_cd
                      )
                      .filter((option) => option.save_trm === 36)[0].intr_rate
                  : "-"
              }}
            </p>
          </td>
        </tr>
      </table>

      <tr v-if="showDetails">
        <td colspan="12">
          <table class="details-table">
            <tr>
              <td class="td1">금융상품설명</td>
              <td>{{ item.etc_note }}</td>
            </tr>
            <tr>
              <td class="td1">가입제한</td>
              <td>{{ item.join_deny }}</td>
            </tr>
            <tr>
              <td class="td1">가입대상</td>
              <td>{{ item.join_member }}</td>
            </tr>
            <tr>
              <td class="td1">가입방법</td>
              <td>{{ item.join_way }}</td>
            </tr>
            <tr>
              <td class="td1">우대조건</td>
              <td>{{ item.spcl_cnd }}</td>
            </tr>
            <tr>
              <td class="td1">만기후이자율</td>
              <td>{{ item.mtrt_int }}</td>
            </tr>
            <tr>
              <td class="td1">최고한도</td>
              <td>{{ item.max_limit }}</td>
            </tr>
          </table>
        </td>
      </tr>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";

const store = useCounterStore();
const filteredDepositList = ref([]);
const filteredSavingList = ref([]);
const bank = ref(null);
const term = ref(null);

onMounted(() => {
  store.getDepositProducts();
  store.getSavingProducts();
});

const filterData = (data) => {
  const data2 = data.filter((d) => d.kor_co_nm === bank.value);
  return data2;
};

const filterData2 = (data, options) => {
  // term 필터링
  const optionList = options.value.filter(
    (option) => option.save_trm === Number(term.value)
  );

  // product 안에 위에서 걸러준 option 이 있으면 반환
  const tmp2 = data.filter((product) => {
    const findProduct = optionList.find(
      (ele) => product.fin_prdt_cd === ele.fin_prdt_cd
    );
    if (findProduct) return true;
  });

  return tmp2;
};

const filterLists = () => {
  filteredDepositList.value = filterData2(
    filterData(store.depositProducts),
    options
  );
  filteredSavingList.value = filterData2(
    filterData(store.savingProducts),
    options2
  );
};

const handleSubmit = () => {
  filterLists();
};

const showDetails = ref(false);

const toggleDetails = () => {
  showDetails.value = !showDetails.value;
};

const options = ref([]);
options.value = store.depositProductsOptions;

const options2 = ref([]);
options2.value = store.savingProductsOptions;
</script>

<style scoped>
.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin: auto;
  max-width: 1000px;
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 30%;
  background-color: #f2f9f9; /* Light background color */
}

.center {
  display: flex;
  flex-wrap: wrap;
  gap: 10px; /* Adjust the gap as needed */
  margin: 20px;
}

.select-wrapper {
  flex: 1; /* Distribute available space equally between select elements */
}

.submit-button {
  padding: 12px 20px;
  font-size: 16px;
  background-color: rgb(0, 75, 76); /* Accent color */
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  border-radius: 5px;
}

.submit-button:hover {
  background-color: #00585b; /* Darker shade on hover */
}

.box-container {
  /* display: flex;
  flex-direction: column;
  gap: 10px;
  height: 30%;
  margin: 100px 20px 100px 0px;
  padding: 10px 10px 150px 10px;
  border-radius: 0px 5px 5px 0px;  */
  /* position: fixed; */
  right: 23%;
  display: flex;
  /*top: 2%;
  background-color: none;
  color: white; 
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);  */
}

.box {
  flex: 1;
  padding: 5px; /* 여백 추가 */
  text-align: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
  border-radius: 0 10px 10px 0;
  width: 100%;
  /* writing-mode: vertical-lr; 
  text-orientation: upright;  */
}

.deposit-box {
  background-color: rgb(0, 75, 76); /* 흰색 배경 */
  color: white; /* 배경과 대조되는 텍스트 색상 */
  margin-bottom: 20px;
  margin-right: 1rem;
}

.saving-box {
  color: white; /* 배경과 대조되는 텍스트 색상 */
}
.box:hover {
  background-color: rgb(0, 75, 76); /* 흰색 배경 */
  color: #fff;
}

.link-wrapper {
  margin-top: 20px; /* Add margin to separate the links from the form */
}

.link-wrapper RouterLink {
  margin-right: 10px; /* Add space between the links */
  text-decoration: none;
  color: #333;
  font-size: 14px;
  transition: color 0.3s ease;
}

.link-wrapper RouterLink:hover {
  color: rgb(0, 75, 76); /* Accent color on hover */
}
.table-container {
  max-width: 1000px;
  margin: auto;
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  background-color: white;
}

.styled-table tr {
  border-bottom: 1px solid #ddd;
}

.styled-table td {
  padding: 12px;
  text-align: left;
}

.styled-table td.label {
  font-weight: bold;
  width: 15%;
}
.styled-table td.bank {
  width: 40%;
}

.styled-table td.product {
  font-weight: bold;
  width: 70%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.details-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.details-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  background-color: white;
}
.td1 {
  font-weight: bold;
  width: 25%;
}

.td2 {
}
.details-label {
  font-weight: bold;
  width: 30%;
}
</style>