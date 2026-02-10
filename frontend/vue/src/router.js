import { createRouter, createWebHistory } from 'vue-router'
import api from './api'

import LoginPage from './pages/LoginPage.vue'
import SignupPage from './pages/SignupPage.vue'
import HomePage from './pages/HomePage.vue'
import SecretPage from './pages/SecretPage.vue'

async function isAuthed() {
  try {
    await api.get('/protected') // если cookie валидна — 200
    return true
  } catch {
    return false
  }
}

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', component: LoginPage },
    { path: '/signup', component: SignupPage },

    // защищённые
    { path: '/', component: HomePage, meta: { requiresAuth: true } },
    { path: '/secret', component: SecretPage, meta: { requiresAuth: true } },

    { path: '/:pathMatch(.*)*', redirect: '/' },
  ],
})

router.beforeEach(async (to) => {
  if (!to.meta.requiresAuth) return true

  const ok = await isAuthed()
  if (!ok) return { path: '/login' }
  return true
})

export default router
