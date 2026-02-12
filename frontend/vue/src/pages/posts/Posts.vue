    <template>
    <Header />
    <h1>Posts</h1>

    <div v-for="value in posts" :key="value.id">
        <p>post title: {{ value.name }}</p>
        <p>user name: {{ value.author.name }}</p>
        <RouterLink :to="`/posts/${value.id}`">Open post</RouterLink>
        <hr>
    </div>

    </template>

    <script setup>
    import Header from '@/components/Header.vue';
    import api from '@/api/api';
    import { onMounted, ref } from 'vue';

    const posts = ref([]);

    onMounted(async () => {
        const res = await api.get("/posts");
        posts.value = res.data;
    })

    </script>
