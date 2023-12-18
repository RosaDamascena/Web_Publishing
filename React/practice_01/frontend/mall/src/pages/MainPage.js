import { Link } from "react-router-dom"
import BasicLayout from "../layouts/BasicLayout"

const MainPage = () => {
    return (
        // <div className="flex">
        //     <Link to={'/about'}>About</Link>
        // </div>
            
        <BasicLayout>
            <div className=" text-3xl">Main Page</div>
        </BasicLayout>
    )
}
export  default MainPage