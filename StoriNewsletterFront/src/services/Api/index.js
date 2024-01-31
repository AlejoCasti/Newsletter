import axios from 'axios';
import router from '../../router';
import Swal from 'sweetalert2'

const conn = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

conn.interceptors.request.use(
  function (config) {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }

    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

conn.interceptors.response.use(
  response => response,
  async function (error) {
    if (error.response && error.response.status === 401) {
      await Swal.fire({
        title: 'Error!',
        text: 'Your credentials have expired',
        icon: 'error',
        confirmButtonColor: '#00D180',
        confirmButtonText: 'Log in',
      })
      localStorage.removeItem('token');
      router.push('/login');
    }
    return Promise.reject(error);
  }
);
export default conn;
