import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/';

export const fetchPosts = async () => {
    const response = await axios.get(`${API_BASE_URL}/posts`);
    return response.data;
};

export const fetchPostById = async (id) => {
    const response = await axios.get(`${API_BASE_URL}/posts/${id}`);
    return response.data;
};

export const createPost = async (post) => {
    const response = await axios.post(`${API_BASE_URL}/posts`, post);
    return response.data;
};

export const updatePost = async (id, updatedPost) => {
    const response = await axios.put(`${API_BASE_URL}/posts/${id}`, updatedPost);
    return response.data;
};

export const deletePost = async (id) => {
    const response = await axios.delete(`${API_BASE_URL}/posts/${id}`);
    return response.data;
};
