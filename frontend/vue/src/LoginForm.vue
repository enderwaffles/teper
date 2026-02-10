<script setup>
import { ref } from 'vue'
import api from './api'

const emit = defineEmits(['success', 'back'])

const name = ref('')
const password = ref('')
const err = ref('')

async function submit() {
  err.value = ''
  try {
    await api.post('/login', { name: name.value, password: password.value })
    emit('success')
  } catch {
    err.value = 'login error'
  }
}
</script>

<template>
  <div>
    <input v-model="name" placeholder="name" />
    <input v-model="password" type="password" placeholder="password" />
    <button @click="submit">Login</button>
    <button @click="$emit('back')">Back</button>
    <div v-if="err">{{ err }}</div>
  </div>
</template>
