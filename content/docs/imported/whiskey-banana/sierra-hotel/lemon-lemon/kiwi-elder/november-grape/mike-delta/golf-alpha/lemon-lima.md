# Play: Lemon - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "lemon_app"
    retry_count: 3

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/lemon/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z
