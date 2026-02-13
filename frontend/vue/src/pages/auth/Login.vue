<template>

  <div class="links">
    <RouterLink to="/signup">
      Don’t have an account?
    </RouterLink>

    <RouterLink to="/">
      ← Back home
    </RouterLink>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()

const name = ref('')
const password = ref('')

async function login() {
  if (!name.value || !password.value) {
    alert('Fill all fields')
    return
  }

  try {
    const res = await api.post('/login', {
      name: name.value,
      password: password.value
    })

    auth.login({
      id: res.data.user.id,
      name: res.data.user.name
    })

    router.push('/')
  } catch (err) {
    alert('Login failed')
  }
}
</script>

<style scoped></style>
