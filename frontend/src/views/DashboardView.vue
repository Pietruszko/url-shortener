<template>
    <div class="min-h-screen w-full bg-black p-8">
        <div class=" border-gray-500 border-2 mx-auto w-160 p-4 rounded-2xl m-32">
            <h1 class="text-center text-2xl text-white">Welcome to your dashboard</h1>
            <h2 class="text-white">Create short url</h2>
            <form @submit.prevent="handleCreateShortUrl" class="input-form">
                <input v-model="shortenedURLForm.original_url" placeholder="Original URL" required class="mr-2 p-1 placeholder-gray-400 bg-white">
                <button class="bg-emerald-400 rounded-3xl p-1.5 m-0.5  hover:bg-emerald-600 text-white w-50">Create Short URL</button>
            </form>
            <h3 class="text-white mt-5">Your URLs:</h3>
            <ul>
                <li v-for="url in urls" :key="url.id" class="url-item">
                    <span>
                        <a :href="`http://127.0.0.1:8000/${url.short_code}`" target="_blank" class="text-white hover:text-gray-300 underline">
                            {{ url.short_code }}
                        </a>
                    </span>
                </li>               
            </ul>
            <button @click="handleLogout" class="bg-emerald-400 rounded-3xl p-1.5 m-0.5  hover:bg-emerald-600 text-white w-50">Logout</button> 
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/auth.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const urls = ref([])
const shortenedURLForm = ref({
    original_url: ''
})

const handleLogout = async () => {
    try {
        localStorage.removeItem('token')
        router.push('/login')
    } catch (error) {
        console.error('Error logging out:', error)
    }
}

const handleCreateShortUrl = async () => {
    try {
        const response = await api.post('/shorten/', shortenedURLForm.value)
        urls.value.push(response.data)
        alert(`Your shortened URL is: 127.0.0.1:8000/${response.data.short_code}`)
    } catch (error) {
        alert('Failed to create short URL')
    }
}

onMounted(fetchUrls)

async function fetchUrls() {
    try {
        const response = await api.get('/shorten/list')
        urls.value = response.data
    } catch (error) {
        console.error('Error fetching URLs:', error)
    }
}
</script>