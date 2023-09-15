import cv2 as cv

__JETT__ = "agents/jett.png"

def locate_agent(agent:str):
    image = cv.imread(agent)
    cv.imshow('Jett', image)
    cv.waitKey(0)



if __name__ == '__main__':
    locate_agent(__JETT__)
    

