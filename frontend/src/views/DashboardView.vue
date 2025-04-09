<template>
    <div class="dashboard-container">
        <h1>Welcome to your dashboard</h1>
        <h2>Create short url</h2>
        <form @submit.prevent="handleCreateShortUrl" class="input-form">
            <input v-model="shortenedURLForm.original_url" placeholder="Original URL" required>
            <button type="submit">Create Short URL</button>
        </form>
        <h3>Your URLs</h3>
        <ul>
            <li v-for="url in urls" :key="url.id" class="url-item">
                <span>
                    <a :href="`http://127.0.0.1:8000/${url.short_code}`" target="_blank">
                        {{ url.short_code }}
                    </a>
                </span>
            </li>               
        </ul>
        <button @click="handleLogout" class="logout-button">Logout</button> 
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
        const response = await api.post('/shorten', shortenedURLForm.value)
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