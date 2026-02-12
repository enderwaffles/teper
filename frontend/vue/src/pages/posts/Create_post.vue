<template>
<Header />
<h1>Create post</h1>
<input type="text" v-model="post_name" placeholder="postname"> <br>
<button type="submit" v-on:click="submit()">submit</button>
</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const post_name = ref("")

async function submit() {
    const res = await api.post("/posts", {
        name: post_name.value
    })
    router.push("/posts")
}

</script>
