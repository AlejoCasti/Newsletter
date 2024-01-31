<template lang="pug">
.form-container
  h3 Create your account
  form.form(@submit.prevent="signUp")
    input(v-model="username", placeholder="Username")
    input(v-model="password", placeholder="Password", type="password")
    span.error(v-show="error") {{ error }}
    button.primary-button(type="submit") Sign up
    router-link(to="/login") Login
</template>

<script>
import AuthService from '../services/Auth';

export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async signUp() {
      try {
        await AuthService.signUp({
          username: this.username,
          password: this.password,
        });

        this.$router.push('/');
      } catch (e) {
        this.error = e.response.data.error;
      }
    },
  },
};
</script>

<style scoped>
h3 {
  color: #002c30;
}

.form-container {
  background: white;
  padding: 40px 20px;
  border-radius: 10px;
  width: 350px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
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

a {
  color: #002c30;
}
</style>
