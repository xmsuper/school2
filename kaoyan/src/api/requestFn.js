import axios from "axios"
import store from '@/store/index.js'
const api = axios.create({
    //配置对象
    //基础的axios地址
    baseURL: 'http://127.0.0.1:8000',
    //超过的时间
    timeout: 5000,
    //预定义请求头，一般工作中这里填写隐藏了客户端身份的字段
    // headers:{'X-Custom-header':'footbar'}
})

// 请求拦截器
api.interceptors.request.use((config) => {
    //在发送请求之前做些什么
    // 例如判断用户的登录状态
    // 登录的判断，如果用户是登录状态，会在headers中把用户的token传递给后端
    // config是个配置对象，对象里有个属性很重要，headers请求头

    //每次发送请求之前，先把等待置为true
        store.commit('setLoading', true)
    return config
}, (error) => {
    return Promise.reject(new Error('fail'))
})

// 响应拦截器  后端给前端的数据（后端返回给前端）
api.interceptors.response.use((response) => {
    //以2开头的状态码都会触发该含函数
    // 对响应数据做点什么
    // 后端给前端数据的时候，会有code码


    //响应完成后，先把等待置为false
        store.commit('setLoading', false)
    return response
}, (error) => {
    return Promise.reject(new Error('fail'))
})

//对外的公开方法
function requestFn(_config) {
    let { url, data, method } = _config;
    url = url || '';
    data = data || {}
    method = method || 'get'

    switch (method) {
        case 'get':
            return api.get(url, { params: data })
        case 'post':
            // return post内容 
            return api.post(url, { params: data })
        default:
        //默认情况
    }
}
export default requestFn;