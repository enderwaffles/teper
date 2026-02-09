
<template>
    <div>
        <p>
            {{ users }} 
        </p>
        <button type="button" v-on:click="deleteUser()">
            delete
        </button>

    </div>

</template>

<script>
export default {
    props: {
        users: {
            type: Object,
            required: true
        },  
        deleteUser: {
            type: Function,
            required: true
        }
    } 
}
</script>

<style>

</style>
