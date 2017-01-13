#if __cplusplus < 201103L
    #error "should use --std=c++11 option."
#endif
#include <iostream>
#include <boost/unordered_map.hpp>
#include <vector>
#include <string>
#include <algorithm>

#include <boost/smart_ptr.hpp>
#include <boost/thread.hpp>
#include <boost/thread/mutex.hpp>
#include <boost/typeof/typeof.hpp>

class Entry{
    public:
        Entry(std::string &w,std::string &u,std::string& p)
            :website_(w),username_(u),password_(p){}

        const std::string & website() const {return website_;}
        void set_website(const std::string& w) {website_ = w;}

        const std::string & username() const {return username_;}
        void set_username(const std::string& u) {username_ = u;}

        const std::string & password() const {return password_;}
        void set_password(const std::string& p){password_ = p;}

        const std::vector<std::string> & tips() const {return tips_;}
        void add_tip(const std::string & k,const std::string & v)
        {
        }
        void del_tip(const std::string& k)
        {
        }

    private:
        std::string website_;
        std::string username_;
        std::string password_;
        std::vector<std::string> tips_;
};


class Manager{
    public:
        /*Manager * get_instance()
        {
            boost::mutex::scoped_lock lck(g_mtx_);
            if(instance_){
                instance_ = new Manager;
            }
        }
        */
        Manager(){}

        ~Manager()
        {
            FILE fp = fopen("passwd_data","w+");
            for(BOOST_AUTO(iter,entries_.begin());iter!=entries_.end():++iter)
            {
                fwrite()

            }
        }

    public:
        bool add_entry(const std::string& website,Entry & entry)
        {
            if(entries_.find(website)==entries_.end())
            {
                entries_[website] = entry;
            }
        }
    private:
        std::unordered_map<std::string,Entry> entries_;
        //static boost::mutex g_mtx_;
        //Manager * instance_;
};
