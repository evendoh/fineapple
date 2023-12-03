import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const userData = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const savingProductsOptions = ref([])
  const depositProductsOptions = ref([])
  // 로그인 시 토큰 저장
  const token = ref(null)
  
  const exchangeRates = ref([])
  const savingProducts = ref([])
  const depositProducts = ref([])
  const wantProducts = ref([])
  const recommendedProduct = ref()

    // 회원가입
    const signup = function (payload) {
      const {
        username,
        password1,
        password2,
        age,
        money,
        saving_possible_money,
        name,
        saving_possible_period,
        financial_type } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          age,
          money,
          saving_possible_money,
          financial_type, name,
          saving_possible_period,
        },
      })
        .then((res) => {
          console.log("회원가입이 완료되었습니다.");
          console.log(res);
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => {
          console.error(err.response.data);
          console.log(err.response.data.username);
          alert("Error: " + err.response.data.username); // Display the error message in an alert
        });
    };

    // 회원 정보 수정
    const updateProfile = (editedProfile) => {
      const { age, money, saving_possible_money, saving_possible_period, financial_type } =
        editedProfile;

      axios({
        method: "put",
        url: `${API_URL}/accounts/user/edit/`,
        data: {
          age,
          money,
          saving_possible_money,
          saving_possible_period, 
          financial_type
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("프로필 업데이트 성공");
          alert("프로필이 성공적으로 업데이트되었습니다.");
          router.push({ name: "ProfileView" });
        })
        .catch((error) => {
          console.error(error.response.data);
          alert("프로필 수정에 실패했습니다.");
          console.log("프로필 업데이트 실패");
        });
    };

    // 금융 상품 추가
    const updateFinancial = (financial_product) => {
      axios({
        method: "put",
        url: `${API_URL}/accounts/user/financial/`,
        data: {
          financial_product,
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("상품 추가 성공");
          alert("금융상품이 성공적으로 업데이트되었습니다.");
          // router.push({ name: 'ProfileView' });
        })
        .catch((error) => {
          console.error(error.response.data);
          alert("금융상품 목록 수정에 실패했습니다.");
          console.log("상품 추가 실패");
        });
    };

    // 금융mbti 저장 및 수정
    const updateMbti = (mbti) => {
      axios({
        method: "put",
        url: `${API_URL}/accounts/user/mbti/`,
        data: {
          mbti,
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("mbti 저장 성공");
          alert("MBTI가 성공적으로 업데이트되었습니다.");
          router.push({ name: 'ProfileView' });
        })
        .catch((error) => {
          console.error(error.response.data);
          alert("MBTI 저장에 실패했습니다.");
          console.log("mbti 저장 실패");
        });
    }

    // 추천 금융 상품 가져오기
    const getProductByMbti = () => {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/recommended_product/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          recommendedProduct.value = res.data
          console.log("추천 금융 상품 완");
          console.log(recommendedProduct.value);
          return res.data;
        })
        .catch((error) => {
          console.error(error.response.data);
          // alert("MBTI 저장에 실패했습니다.");
          console.log("금융 상품 추천 실패");
        });
    }





    // 비밀번호 수정
    const changePassword = (new_password1, new_password2) => {
      axios({
        method: "post",
        url: `${API_URL}/accounts/password/change/`,
        data: {
          new_password1,
          new_password2,
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("비밀번호 변경 성공");
          alert("비밀번호 변경이 완료되었습니다!");
          router.push({ name: "ProfileView" });
        })
        .catch((error) => {
          console.error(error.response.data);
          alert("비밀번호 변경에 실패했습니다.");
          console.log("프로필 업데이트 실패");
        });
    };

    // 회원 탈퇴
    const withdrawMembership = () => {
      axios({
        method: "delete",
        url: `${API_URL}/accounts/user/edit/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          token.value = null;
          console.log("회원 탈퇴 성공");
          alert("회원 탈퇴가 성공적으로 처리되었습니다.");
          router.push({ name: "home" });
        })
        .catch((error) => {
          console.error(error.response.data);
          console.log("회원 탈퇴 실패");
          alert("회원 탈퇴에 실패했습니다.");
        });
    };

    // 로그인
    const logIn = function (payload) {
      const { username, password } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log("로그인이 완료되었습니다");
          console.log(res);
          token.value = res.data.key;
          getUserProfile();
          router.push({ name: "home" });
          console.log("완료");
        })
        .catch((err) => console.log(err.response.data));
    };

    // 로그인되있는지 확인
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    // 프로필 불러오기
    const getUserProfile = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((response) => {
          console.log("유저 프로필 조회 결과:", response.data);
          // 여기서 받아온 프로필 정보를 활용하면 됩니다.
          userData.value = response.data;
        })
        .catch((error) => {
          console.log("유저 프로필 조회 실패:", error.response.data);
        });
    };

    // 로그아웃
    const logOut = async () => {
      await axios({
        method: "post", // 로그아웃은 보통 POST 요청으로 수행됩니다.
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then(() => {
          token.value = null; // 토큰 초기화
          wantProducts.value = [];
          userData.value = null;
          router.push({ name: "home" }); // 로그아웃 후 홈으로 리다이렉트
            })
        .catch((error) => console.error(error));
    };

    // DRF에 article 조회 요청을 보내는 action
    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/articles/`,
      })
        .then((response) => {
          // console.log(response)
          articles.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    // DRF에 환율 조회 요청을 보내는 action
    const getExchangeRates = function () {
      axios({
        method: "get",
        url: `${API_URL}/exchange/`,
      })
        .then((response) => {
          // console.log(response)
          exchangeRates.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    // DRF에 적금정보 조회 요청을 보내는 action
    const getSavingProducts = function () {
      axios({
        method: "get",
        url: `${API_URL}/financial/saving_products/`,
      })
        .then((response) => {
          console.log(response.data);
          savingProducts.value = response.data.saving_product;
          savingProductsOptions.value = response.data.saving_product_options;
          // console.log(savingProducts.value)
        })
        .catch((error) => {
          console.log(error);
        });
    };

  // DRF에 예금정보 조회 요청을 보내는 action
  const getDepositProducts = function() {
  axios({
    method: 'get',
    url: `${API_URL}/financial/deposit_products/`
  })
  .then((response) => {
    console.log(response.data)
    depositProducts.value = response.data.deposit_product
    depositProductsOptions.value = response.data.deposit_product_options
    console.log(depositProducts.value)
  })
  .catch((error) => {
    console.log(error)
  })
  }




  return { signup, logIn, getUserProfile, updateProfile, updateFinancial, updateMbti, getProductByMbti, changePassword, withdrawMembership, isLogin, logOut, userData, token, exchangeRates, savingProducts, savingProductsOptions, depositProducts, depositProductsOptions, API_URL, articles, wantProducts, recommendedProduct, getArticles, getExchangeRates, getSavingProducts, getDepositProducts }
}, { persist: true })