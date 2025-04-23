<template>
    <div class="min-h-screen w-full bg-black p-8">
        <div class=" border-gray-500 border-2 mx-auto w-160 p-4 rounded-2xl m-32">
            <h1 class="text-center text-2xl text-white mb-2">Register</h1>
            <form @submit.prevent="handleRegister" class="auth-form">
                <input v-model="form.username" placeholder="Username" required class="mr-2 p-1 placeholder-gray-400 bg-white">
                <input v-model="form.password" type="password" placeholder="Password" required class="mr-2 p-1 placeholder-gray-400 bg-white">
                <input v-model="form.confirmPassword" type="password" placeholder="Confirm Password" required class=" mt-2 mr-2 p-1 placeholder-gray-400 bg-white">
                <button class="bg-emerald-400 rounded-3xl p-1.5 m-0.5  hover:bg-emerald-600 text-white w-20">Register</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import api from '@/auth.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
    username: '',
    password: '',
    confirmPassword: ''
})

onMounted(() => {
    if (localStorage.getItem('token')) {
        router.push('/dashboard')
    }
})

const handleRegister = async () => {
    try {
        const response = await api.post('register/', {
            username: form.value.username,
            password: form.value.password
        })
        router.push('/login')
    } catch (error) {
        alert('Registration failed!')
    }
}
</script>