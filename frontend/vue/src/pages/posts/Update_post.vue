<template>
<h1>Update post</h1>


<input v-model="title" placeholder="Title" />
<br>
<input v-model="text" placeholder="Text"/>
<br>

<button @click="send()">Send</button>
</template>

<script setup>
import api from '@/api/api'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const post_id = route.params.id

const title = ref("")
const text = ref("")

// отправка
async function send() {

  await api.patch(`/posts/${post_id}`, {
    title: title.value,
    text: text.value,

  })

  router.push(`/posts/${post_id}`)
}
</script>

<style scoped>
</style>
