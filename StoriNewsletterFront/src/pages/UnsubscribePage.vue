<template lang="pug">
.unsubscribe-container
  h3 Unsubscribe
  span Hold on a moment! 😱 Before you say goodbye, we wanted to remind you that in our corner, you'll always find interesting news and exclusive content. Why not give it one last shot? 😎 Before you go, are you sure you want to unsubscribe? We want to make sure you don't miss out on the exciting updates coming your way. We invite you to stick around a bit longer with us!
  .call-to-action
    button.primary-button(@click="goToHome") Cancelar
    button.secondary-button(@click="unsubscribe") Unsubscribe
</template>
<script>
import apiService from '../services/Api/apiController';
import Swal from 'sweetalert2'

export default {
  name: 'UnsubscribePage',
  methods: {
    async unsubscribe() {
      try {
        const token = this.$route.params.token;
        await apiService.unsubscribe({ token });

        await Swal.fire({
          title: 'We hope to see you back soon!',
          text: 'You have successfully unsubscribe',
          icon: 'success',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        })

        window.close();
      } catch (e) {
        if (e.response && e.response.status === 401) return;
        Swal.fire({
          title: 'Error!',
          text: 'An error occurred during the process. Please try again later.',
          icon: 'error',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        })
      }
    },
    async goToHome() {
      await Swal.fire({
        title: 'Thanks!',
        text: "We're so happy you're sticking around! Count on us to keep the good vibes!",
        icon: 'success',
        confirmButtonColor: '#00D180',
        confirmButtonText: 'Continue',
      })
      window.close();
    }
  }
};
</script>
<style scoped>
.unsubscribe-container {
  background: white;
  padding: 40px 20px;
  border-radius: 10px;
  width: 700px;
  display: flex;
  flex-direction: column;
  /* gap: 20px; */
}

.call-to-action{
  margin-top: 20px;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
</style>