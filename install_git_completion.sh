#!/bin/bash

rm -f git-completion.bash

wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash

cp git-completion.bash ~/git-completion.bash


echo "if [ -f ~/git-completion.bash ];then\n\
    source ~/git-completion.bash\n\
fi\n" >> ~/.bashrc

git config --global alias.co checkout

git config --global alias.br branch

git config --global alias.ci commit

git config --global alias.st status

