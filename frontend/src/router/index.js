import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'


const routes = [
  {
    path: '/',
    redirect: 'login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
    meta: { forGuestOnly: true }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
