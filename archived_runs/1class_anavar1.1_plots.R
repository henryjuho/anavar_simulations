library(ggplot2)
library(dplyr)

args <- commandArgs(TRUE)
input_file = args[1]

test_data = subset(read.delim(input_file), sim_e_1 != 0)

summarised_theta = summarise(group_by(test_data, sim_theta_1, sim_e_1), 
                             meanTheta = mean(data_1_theta_1), 
                             lwr=quantile(data_1_theta_1, probs=0.025), 
                             upr=quantile(data_1_theta_1, probs=0.975))

summarised_gamma = summarise(group_by(test_data, sim_gamma_1, sim_e_1),
                             meanGamma = mean(data_1_gamma_1),
                             lwr=quantile(data_1_gamma_1, probs=0.025),
                             upr=quantile(data_1_gamma_1, probs=0.975))

summarised_error = summarise(group_by(test_data, sim_e_1),
                             meanE = mean(data_1_e_1),
                             lwr=quantile(data_1_e_1, probs=0.025),
                             upr=quantile(data_1_e_1, probs=0.975))

theta <- ggplot(summarised_theta, aes(x=sim_theta_1, y=meanTheta)) + 
  geom_point(stat='identity') +
  geom_pointrange(aes(ymin=lwr, ymax=upr)) +
  geom_abline(intercept=0, slope=1, colour='tomato3') +
  theme_bw(base_size = 10) +
  facet_wrap(~sim_e_1, ncol = 3) +
  labs(x=expression(theta[simulated]), y=expression(theta[predicted])) +
  theme(axis.title = element_text(size = 20, face = 'bold'),
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_text(size = 13, face = 'bold'))

ggsave('1class.1snps.anavar1.1.theta.jpg', theta, width=15, height=7)

gamma <- ggplot(summarised_gamma, aes(x=sim_gamma_1, y=meanGamma)) +
geom_point(stat='identity') +
geom_pointrange(aes(ymin=lwr, ymax=upr)) +
geom_abline(intercept=0, slope=1, colour='tomato3') +
theme_bw(base_size = 10) +
facet_wrap(~sim_e_1, ncol = 3) +
labs(x=expression(gamma[simulated]), y=expression(gamma[predicted])) +
theme(axis.title = element_text(size = 20, face = 'bold'),
     axis.text = element_text(size = 15, face = 'bold'),
     strip.text.x = element_text(size = 13, face = 'bold'))

ggsave('1class.1snps.anavar1.1.gamma.jpg', gamma, width=15, height=7)

error <- ggplot(summarised_error, aes(x=sim_e_1, y=meanE)) +
geom_point(stat='identity') +
geom_pointrange(aes(ymin=lwr, ymax=upr)) +
geom_abline(intercept=0, slope=1, colour='tomato3') +
theme_bw(base_size = 10) +
labs(x=expression(e[simulated]), y=expression(e[predicted])) +
theme(axis.title = element_text(size = 20, face = 'bold'),
     axis.text = element_text(size = 15, face = 'bold'),
     strip.text.x = element_text(size = 13, face = 'bold'))

ggsave('1class.1snps.anavar1.1.error.jpg', error, width=7, height=7)
