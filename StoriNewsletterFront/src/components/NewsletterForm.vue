<template lang="pug">
.form-container
  input(v-model="title" placeholder="Title")
  div
    .email-section
      input(v-model="currentEmail" placeholder="Add email")
      button.primary-button(@click="addEmail") +
    span.error(v-if="emailError") {{ emailError }}

  .email-list(v-if="emailList.length > 0")
    .email-item(v-for="(email, idx) in emailList" :key="idx") {{ email }}
      i.material-symbols-outlined.delete-icon(@click="() => deleteEmail(idx)") close

  dropzone(
    :formFile="file"
    @onUpload="onUploadFile"
    @onDelete="onDeleteFile"
    )

  .call-to-action
    button.primary-button(@click="saveNewsletter") Save
    span.error(v-if="formError") {{ formError }}
</template>
<script>
import Dropzone from './Dropzone.vue';
import s3Service from '../services/S3/s3Controller';
import apiService from '../services/Api/apiController';
import Swal from 'sweetalert2';

export default {
  name: 'NewsletterForm',
  components: { Dropzone },
  data() {
    return {
      title: '',
      currentEmail: '',
      emailList: [],
      file: null,
      formError: null,
      emailError: null,
      isValidating: false,
    };
  },
  watch: {
    file() {
      this.validateForm();
    },
    emailList() {
      this.validateForm();
    },
    title() {
      this.validateForm();
    },
  },
  methods: {
    addEmail() {
      this.emailError = null;
      const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      if (!String(this.currentEmail).toLowerCase().match(emailRegex)) {
        this.emailError = 'Email is not valid';
        return;
      }

      if (this.emailList.find((email) => email === this.currentEmail)) {
        this.emailError = 'Email is added';
        return;
      }

      this.emailList = [...this.emailList, this.currentEmail];
      this.currentEmail = '';
    },
    deleteEmail(idx) {
      const newArray = this.emailList
      newArray.splice(idx, 1);
      this.emailList = newArray;
    },
    handleFileUpload(e) {
      this.file = e.target.files[0];
    },
    onUploadFile(file) {
      this.file = file;
    },
    onDeleteFile() {
      this.file = null;
    },
    validateForm() {
      this.formError = null;
      if (!this.isValidating) return true;

      if (!this.title || !this.file || this.emailList.length == 0) {
        this.formError = 'There are incomplete fields';
        return false;
      }
      return true;
    },
    async saveNewsletter() {
      try {
        this.isValidating = true;
        const isValidForm = this.validateForm();
        if (!isValidForm) return;

        s3Service.sendFile({ file: this.file });
        await apiService.createNewsletter({
          title: this.title,
          emails: this.emailList.join(','),
          fileName: this.file.name,
        });
        this.$emit('refreshData');
        Swal.fire({
          title: 'Newsletter created',
          text: 'Check the newsletter list to send emails',
          icon: 'success',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        });
        this.clearError();
        this.cleanData();
      } catch (e) {
        if (e.response && e.response.status === 401) return;
        Swal.fire({
          title: 'Error!',
          text: 'An error occurred during the process. Please try again later.',
          icon: 'error',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        });
        this.clearError();
      }
    },
    cleanData() {
      this.file = null;
      this.title = null;
      this.currentEmail = null;
      this.emailList = [];
    },
    clearError() {
      this.formError = null;
      this.emailError = null;
      this.isValidating = false;
    },
  },
};
</script>
<style scoped>
.form-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.email-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

input {
  background-color: white;
  border: 1px solid #cccccc;
  border-radius: 4px;
  width: 100%;
  color: #002c30;
  font-size: 14px;
  padding: 10px 10px;
  box-sizing: border-box;
}

.email-list {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 5px;
}

.email-item {
  background-color: #002c30;
  color: white;
  padding: 10px;
  border-radius: 15px;
  box-sizing: border-box;
  font-size: 12px;
  display: flex;
  justify-content: flex-end;
  align-items: start;
  gap: 5px;
}
.call-to-action {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.delete-icon {
  color: white;
  font-size: 10px;
}
</style>
