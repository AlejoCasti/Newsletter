import ApiService from '../Api/apiController';

export default {
  async login({ username = '', password = '' }) {
    const { data } = await ApiService.login({ username, password });
    localStorage.setItem('token', data.token);
  },
  async signUp({ username = '', password = '' }) {
    const { data } = await ApiService.signUp({ username, password });
    localStorage.setItem('token', data.token);
  },
  async logout() {
    await ApiService.logout();
    localStorage.removeItem('token');
  },
};
