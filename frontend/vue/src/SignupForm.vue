<script setup>
import { ref } from 'vue'
import api from './api'

const emit = defineEmits(['back', 'done'])

const name = ref('')
const password = ref('')
const msg = ref('')
const err = ref('')

async function submit() {
  msg.value = ''
  err.value = ''
  try {
    await api.post('/signup', { name: name.value, password: password.value })
    msg.value = 'ok'
    emit('done') // после регистрации перекинет на login
  } catch {
    err.value = 'signup error'
  }
}
</script>

<template>
  <div>
    <input v-model="name" placeholder="name" />
    <input v-model="password" type="password" placeholder="password" />
    <button @click="submit">Signup</button>
    <button @click="$emit('back')">Back</button>
    <div v-if="msg">{{ msg }}</div>
    <div v-if="err">{{ err }}</div>
  </div>
</template>
