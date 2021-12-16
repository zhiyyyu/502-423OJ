<template>
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div>
        <div v-for="problemlist in info.results" v-bind:key="problemlist.url" id="problemlist">
            
            <div class="problemlist-title">
                {{ problemlist.title }}
            </div>
            <!-- <div>
                <span 
                    v-for="tag in problemlist.tags" 
                    v-bind:key="tag" 
                    class="tag"
                >
                    {{ tag }}
                </span>
            </div>

            <div>{{ formatted_time(problemlist.created) }}</div> -->
        </div>
    </div>
</template>

<script>
    // import HelloWorld from './components/HelloWorld.vue'
    // export default {
    //     name: 'App',
    //     components: {
    //         HelloWorld
    //     }
    // }

    import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                info: ''
            }
        },
        mounted() {
            axios
                .get('/api/problemlist/')
                .then(response => (this.info = response.data))
        }
    }

</script>

<style>
    /* #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    } */
    #articles {
        padding: 10px;
    }

    .problemlsit-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
</style>