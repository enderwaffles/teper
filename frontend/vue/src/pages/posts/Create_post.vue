<template>
<Header />
<h1>Create post</h1>
<input type="text" v-model="post_title" placeholder="postname"> <br>
<button type="submit" v-on:click="submit()">submit</button>
</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const post_title = ref("")

async function submit() {
    const res = await api.post("/posts", {
        title: post_title.value
    })
    router.push("/posts")
}

</script>
