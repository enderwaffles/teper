
<template>
    <h1>{{ title }}</h1>
    <h1>{{ fullname1 }}</h1>
    <input type="text" placeholder="name" v-model="name">
    <input type="text" placeholder="surname" v-model="surname">
    <button v-on:click="click()">Click</button>
</template>

<script setup>
import { computed, ref, watch } from 'vue';

defineProps ({
    title: String,
})

const emit = defineEmits(["submit"])
const name = ref("")
const surname = ref("")
const fullname1 = ref("")

watch(fullname1, (newValue, oldValue) => {
    console.log("was:", oldValue)
    console.log("came:", newValue)
})

const fullname = computed(() => {
    return name.value + " " + surname.value;
})

function click() {
    console.log("clicked")
    fullname1.value = fullname.value;
    

    emit("submit", fullname.value)
}

</script>

