<template>
  <Header />

  <div>
    <h1>Create post</h1>
  </div>

  <div>
    <input type="text" v-model="title" placeholder="Title">
    <input type="text" v-model="text" placeholder="Text">
    <input type="file" multiple v-on:change="onFileChange">

    <button v-on:click="send">Send</button>
  </div>

</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()


//data
let title = ref("")
let text = ref("")
let files = ref([])

let message = ref("")

//functions
function onFileChange(e) {
  files.value = Array.from(e.target.files)
}

async function send() {

  let form = new FormData()
  form.append("title", title.value)
  form.append("text", text.value)
  
  // if (files.value) {
  //   form.append("uploads", files.value)
  // }

  files.value.forEach(file => {
    form.append("files", file)
  })
  
  const res = await api.post("/posts", form)
  router.push("/posts")
  message = res
}

</script>


<style scoped>

</style>
