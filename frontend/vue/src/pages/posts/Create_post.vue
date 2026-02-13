<template>
  <Header />

  <h1>Create post</h1>

  <input type="text" v-model="post_title" placeholder="postname"> <br>

  <input type="file" @change="onFileChange" /> <br>

  <button type="submit" @click="submit">submit</button>
</template>


<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const post_title = ref("")
const file = ref(null)


function onFileChange(e) {
  file.value = e.target.files[0]
}


async function submit() {
  const form = new FormData()

  form.append("title", post_title.value)

  if (file.value) {
    form.append("file", file.value)
  }

  await api.post("/posts", form, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  })

  router.push("/posts")
}
</script>
  