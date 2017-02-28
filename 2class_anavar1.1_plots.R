library(ggplot2)
library(dplyr)
library(gridExtra)

args <- commandArgs(TRUE)
input_file = args[1]
test_data = subset(read.delim(input_file), sim_e_1 != 0)

# need data in format: simt1 simt2 simg1 simg2 sime1 sime2 t1 t2 g1 g2 e1 e2
tidy_data = data.frame()

for(x in 1:length(test_data$sim_theta_1)){
  line = test_data[x,]
  st1 = line$sim_theta_1
  st2 = line$sim_theta_2
  sg1 = line$sim_gamma_1
  sg2 = line$sim_gamma_2
  se1 = line$sim_e_1
  se2 = line$sim_e_2
  if(abs(st1-line$data_1_theta_1) < abs(st1-line$data_1_theta_2)){
    dt1=line$data_1_theta_1
    dt2=line$data_1_theta_2
  }else{
    dt1=line$data_1_theta_2
    dt2=line$data_1_theta_1
  }
  if(abs(sg1-line$data_1_gamma_1) < abs(sg1-line$data_1_gamma_2)){
    dg1=line$data_1_gamma_1
    dg2=line$data_1_gamma_2
  }else{
    dg1=line$data_1_gamma_2
    dg2=line$data_1_gamma_1
  }
  if(abs(se1-line$data_1_e_1) < abs(se1-line$data_1_e_2)){
    de1=line$data_1_e_1
    de2=line$data_1_e_2
  }else{
    de1=line$data_1_e_2
    de2=line$data_1_e_1
  }
  tidy_data = rbind(tidy_data, c(st1, st2, sg1, sg2, se1, se2, dt1, dt2, dg1, dg2, de1, de2))
}
colnames(tidy_data) = c('st1', 'st2', 'sg1', 'sg2', 'se1', 'se2', 'dt1', 'dt2', 'dg1', 'dg2', 'de1', 'de2')

summarised_theta1 = summarise(group_by(tidy_data, st1, st2), 
                             meanTheta = mean(dt1), 
                             lwr=quantile(dt1, probs=0.025), 
                             upr=quantile(dt1, probs=0.975))

summarised_theta2 = summarise(group_by(tidy_data, st1, st2), 
                              meanTheta = mean(dt2), 
                              lwr=quantile(dt2, probs=0.025), 
                              upr=quantile(dt2, probs=0.975))

theta1 <- ggplot(summarised_theta1, aes(x=st1, y=meanTheta)) + 
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_abline(intercept=0, slope=1, colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~st2,labeller = label_bquote(theta[2] == .(st2))) +
  labs(x='', y=expression(hat(theta[1]))) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        axis.text.x = element_blank(),
        strip.text.x = element_text(size = 13, face = 'bold'))

theta2 <- ggplot(summarised_theta2, aes(x=st1, y=meanTheta)) + 
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_hline(aes(yintercept = st2), colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~st2) +
  labs(x=expression(theta[1]), y=expression(hat(theta[2]))) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_blank())

theta = grid.arrange(theta1, theta2)
ggsave('2class.1snps.anavar1.1.theta.jpg', theta, width=15, height=14)

summarised_gamma1 = summarise(group_by(tidy_data, sg1, sg2),
                             meanGamma = mean(dg1),
                             lwr=quantile(dg1, probs=0.025),
                             upr=quantile(dg1, probs=0.975))

summarised_gamma2 = summarise(group_by(tidy_data, sg1, sg2),
                              meanGamma = mean(dg2),
                              lwr=quantile(dg2, probs=0.025),
                              upr=quantile(dg2, probs=0.975))

gamma1 <- ggplot(summarised_gamma1, aes(x=sg1, y=meanGamma)) + 
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_abline(intercept=0, slope=1, colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~sg2,labeller = label_bquote(gamma[2] == .(sg2))) +
  labs(x='', y=expression(hat(gamma[1]))) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        axis.text.x = element_blank(),
        strip.text.x = element_text(size = 13, face = 'bold'))

gamma2 <- ggplot(summarised_gamma2, aes(x=sg1, y=meanGamma)) + 
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_hline(aes(yintercept = sg2), colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~sg2) +
  labs(x=expression(gamma[1]), y=expression(hat(gamma[2]))) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_blank())

gamma = grid.arrange(gamma1, gamma2)

ggsave('2class.1snps.anavar1.1.gamma.jpg', gamma, width=15, height=14)

summarised_e1 = summarise(group_by(tidy_data, se1, se2),
                              meane = mean(de1),
                              lwr=quantile(de1, probs=0.025),
                              upr=quantile(de1, probs=0.975))

summarised_e2 = summarise(group_by(tidy_data, se1, se2),
                              meane = mean(de2),
                              lwr=quantile(de2, probs=0.025),
                              upr=quantile(de2, probs=0.975))

e1 <- ggplot(summarised_e1, aes(x=se1, y=meane)) + 
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_abline(intercept=0, slope=1, colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~se2,labeller = label_bquote(e[2] == .(se2))) +
  labs(x='', y=expression(hat(e[1]))) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        axis.text.x = element_blank(),
        strip.text.x = element_text(size = 13, face = 'bold'))

e2 <- ggplot(summarised_e2, aes(x=se1, y=meane)) + 
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_hline(aes(yintercept = se2), colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~se2) +
  labs(x=expression(e[1]), y=expression(hat(e[2]))) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_blank())

error = grid.arrange(e1, e2)

ggsave('2class.1snps.anavar1.1.error.jpg', error, width=15, height=14)
