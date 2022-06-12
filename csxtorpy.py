# TODO solve japanese and chinese text problem
# TODO recognize language
# TODO skip empty lines and unneeded languages
# TODO recognize character
# TODO modify character to Ren'Py
# TODO transform csx dialogue to Ren'Py dialogue
# TODO easy to use cli/gui menu

import re

ascii_art = ("""
    ******   ******** **     **   **            *******   *******  **    **
  **////** **////// //**   **   /**           /**////** /**////**//**  ** 
 **    // /**        //** **   ******  ****** /**   /** /**   /** //****  
/**       /*********  //***   ///**/  **////**/*******  /*******   //**   
/**       ////////**   **/**    /**  /**   /**/**///**  /**////     /**   
//**    **       /**  ** //**   /**  /**   /**/**  //** /**         /**   
 //******  ********  **   //**  //** //****** /**   //**/**         /**   
  //////  ////////  //     //    //   //////  //     // //          //    
 **                      **          **                       **     **   
/**       **   **       /**         /**                      /**    //    
/**      //** **        /**  ****** /**       ******   ******/**  ** **   
/******   //***         /** **////**/******  **////** **//// /** ** /**   
/**///**   /**          /**/**   /**/**///**/**   /**//***** /****  /**   
/**  /**   **       **  /**/**   /**/**  /**/**   /** /////**/**/** /**   
/******   **       //***** //****** /**  /**//******  ****** /**//**/**   
/////    //         /////   //////  //   //  //////  //////  //  // //                                                                             
""")                                                                                                                                                       

print(ascii_art)                                                                                                                                              
# reads data from txt
while True:
    filename1 = input("Name of the text file to read: ")
    if not re.match(".+\.txt", filename1):
        print ("Error! Make sure you select a txt file.")
    else:
        filename2 = input("Name of the output text file: ")
        file2 = open(filename2, "w")
        with open(filename1, "r") as file1:
            while (line := file1.readline()):
                patterneng = re.sub("\[EN\d+\]\s*",' "x "', line)
                announcement = re.sub("\[Announcment+\]\s*", 'an "', patterneng)
                haruka = re.sub("\[Haruka+\]\s*",'h "', announcement)
                sora = re.sub("\[Sora+\]\s*",'s "', haruka)
                file2.writelines(sora)
                print(sora)
                break