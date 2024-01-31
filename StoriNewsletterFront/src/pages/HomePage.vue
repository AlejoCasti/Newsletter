<template lang="pug">
.home-container
  loader(v-if="isLoading")
  .header
    router-link.statistics-icon(to="/dashboard")
      i.material-symbols-outlined monitoring

    h3 Admin newspaper

  .form-newsletter
    .expandable-title(@click="switchFormNewsletter")
      span Create your newsletter
      i.material-symbols-outlined {{ !isFormNewsletterExpanded ? 'expand_more' : 'expand_less' }}

    template(v-if="isFormNewsletterExpanded")
      .hr
      newsletter-form(@refreshData="getNewsletters")

  .list-newsletter
    newsletter-list(:newsletters="newsletters" @onSendClick="sendEmail" @onDeleteNewsletter="deleteNewsletter")

  button.primary-button(@click="logout") Logout

</template>
<script>
import NewsletterForm from '../components/NewsletterForm.vue';
import NewsletterList from '../components/NewsletterList.vue';
import Loader from '../components/Loader.vue';

import apiService from '../services/Api/apiController';
import authService from '../services/Auth'

import Swal from 'sweetalert2'

export default {
  name: 'HomePage',
  components: { NewsletterForm, NewsletterList, Loader },
  data() {
    return {
      isFormNewsletterExpanded: true,
      isListNewsletterExpanded: true,
      newsletters: [],
      isLoading: false,
    };
  },
  async mounted() {
    this.getNewsletters();
  },
  methods: {
    switchFormNewsletter() {
      this.isFormNewsletterExpanded = !this.isFormNewsletterExpanded;
    },
    switchListNewsletter() {
      this.isListNewsletterExpanded = !this.isListNewsletterExpanded;
    },
    async sendEmail(id) {
      try {
        this.isLoading = true;
        await apiService.sendEmail({ id });
        Swal.fire({
          title: 'Nesletter sent',
          text: 'The newspaper was distributed successfully',
          icon: 'success',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        })
      } catch (e) {
        if (e.response && e.response.status === 401) return;
        Swal.fire({
          title: 'Error!',
          text: 'An error occurred during the process. Please try again later.',
          icon: 'error',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        })
      } finally {
        this.isLoading = false;
      }
    },
    async getNewsletters() {
      try {
        const { data } = await apiService.getNewsletters();
        if (Array.isArray(data)) {
          this.newsletters = data.map(newsletter => {
            return {
              ...newsletter,
              recipients_emails: newsletter.recipients_emails.join(', ')
            }
          });
        }
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
    async deleteNewsletter(id) {
      try {
        const response = await Swal.fire({
          title: 'Deletion Confirmation!',
          text: 'Are you sure you want to delete this newspaper?',
          icon: 'info',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
          denyButtonText: 'Cancel',
          showDenyButton: true,
        })
        if (!response.value) return;

        await apiService.deleteNewsletter({ id });
        await this.getNewsletters();
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
    async logout() {
      await authService.logout();
      this.$router.push('/login');
    }
  },
};
</script>
<style scoped>
.home-container {
  background: white;
  padding: 40px 20px;
  border-radius: 10px;
  width: 700px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.header {
  display: flex;
  flex-direction: column;
}
.form-newsletter {
  border: 1px solid #cccccc;
  padding: 10px 10px;
  border-radius: 10px;
  box-sizing: border-box;
}

.list-newsletter {
  /* border: 1px solid #cccccc; */
  /* padding: 10px 10px; */
  border-radius: 10px;
  box-sizing: border-box;
}

.material-symbols-outlined {
  display: block;
}

.expandable-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
}

.hr {
  margin: 10px 0px 20px;
  border-bottom: 1px solid #cccccc;
}

.statistics-icon {
  border: 1px solid #cccccc;
  border-radius: 5px;
  align-self: flex-end;
}
</style>
