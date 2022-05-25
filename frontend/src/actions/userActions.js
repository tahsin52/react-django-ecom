import { USER_LOGIN_REQUEST, USER_LOGOUT, USER_LOGIN_FAIL, USER_LOGIN_SUCCESS } from "../constants/userConstants";
import {PRODUCT_DETAILS_FAIL} from "../constants/productConstants";
import axios from "axios";

export const login = (email, password) => async (dispatch) => {
    try{
        dispatch({
            type: USER_LOGIN_REQUEST
        })

        const config = {
            headers:{
                'Content-type': 'application/json'
            }
        }

        const {data} = await  axios.post(
            '/users/login/',
            {'username': email, 'password': password},
            config
        )

        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })

        localStorage.setItem('userInfo', JSON.stringify(data))

    }catch (error) {
        dispatch({
            type: USER_LOGIN_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}

export const logout = () => {

}