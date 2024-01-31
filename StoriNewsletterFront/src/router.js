import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './pages/HomePage.vue';
import LoginPage from './pages/LoginPage.vue';
import RegisterPage from './pages/RegisterPage.vue';
import UnsubscribePage from './pages/UnsubscribePage.vue';
import DashboardPage from './pages/DashboardPage.vue';

const requiredAuth = (to, from, next) => {
  const token = localStorage.getItem('token');

  if (!token) {
    next('/login');
    return;
  }
  
  next();
};

const checkAuth = (to, from, next) => {
  const token = localStorage.getItem('token');

  if (token) {
    next('/');
    return;
  }
  
  next();
};

const routes = [
  { path: '/', component: HomePage, beforeEnter: requiredAuth },
  { path: '/login', component: LoginPage, beforeEnter: checkAuth },
  { path: '/register', component: RegisterPage, beforeEnter: checkAuth },
  { path: '/dashboard', component: DashboardPage, beforeEnter: requiredAuth },
  { path: '/unsubscribe/:token', component: UnsubscribePage }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
